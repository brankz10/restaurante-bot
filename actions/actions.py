import logging
from typing import Any, Dict, List, Text, Union, Optional

import pandas as pd
from pathlib import Path
import datetime

from rasa_sdk import Action, Tracker
from rasa_sdk.forms import FormAction
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import EventType, SlotSet

logger = logging.getLogger(__name__)
orders_dir = Path("orders/")
orders_dir.mkdir(parents=True, exist_ok=True)


class DishForm(FormAction):
    """collects orders and adds them to the database"""

    def name(self) -> Text:
        return "dish_form"

    @staticmethod
    def required_slots(tracker) -> List[Text]:
        return ["dish", "number", "observation", "confirmed"]

    def slot_mappings(self) -> Dict[Text, Union[Dict, List[Dict]]]:
        return {
            "dish": [self.from_entity(entity="dish"),],
            "number": [
                self.from_entity(entity="number", intent=["order"]),
                self.from_intent(intent="order", value=1),
            ],
            "observation": [
                self.from_intent(intent="deny", value="Nenhuma observação"),
                self.from_text(intent="observation"),
            ],
            "confirmed": self.from_entity(entity="confirmed"),
        }

    def validate_dish(
        self,
        value: Text,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> Dict[Text, Any]:
        """Validate dish value."""
        if isinstance(value, list):
            dispatcher.utter_message(
                text="Por favor peça um item por vez, senão eu me confundo."
            )
            return {"dish": None}
        else:
            return {"dish": value}

    def submit(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[EventType]:
        """Once we have all the information, attempt to add it to the
        database"""
        confirmed = tracker.get_slot("confirmed")
        if confirmed:
            data = {
                "dish": [tracker.get_slot("dish")],
                "number": [tracker.get_slot("number")],
                "observation": [tracker.get_slot("observation")],
                "date": [datetime.datetime.now().strftime("%d/%m/%Y")],
            }
            df = pd.DataFrame(data)
            if (orders_dir / f"{tracker.sender_id}.csv").exists():
                df = pd.concat(
                    [pd.read_csv(orders_dir / f"{tracker.sender_id}.csv"), df]
                )
            df.to_csv(orders_dir / f"{tracker.sender_id}.csv", index=False)
            dispatcher.utter_message(template="utter_order_confirmed")
            return [
                SlotSet("dish", None),
                SlotSet("number", None),
                SlotSet("observation", None),
                SlotSet("confirmed", None),
            ]
        else:
            dispatcher.utter_message(template="utter_order_canceled")
            return [
                SlotSet("dish", None),
                SlotSet("number", None),
                SlotSet("observation", None),
                SlotSet("confirmed", None),
            ]


class ActionShowOrders(Action):
    def name(self) -> Text:
        return "action_show_orders"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[EventType]:
        if (orders_dir / f"{tracker.sender_id}.csv").exists():
            dispatcher.utter_message(
                text=str(
                    pd.read_csv(orders_dir / f"{tracker.sender_id}.csv")
                )
            )
        else:
            dispatcher.utter_message(text="Você ainda não fez nenhum pedido.")
        return []
