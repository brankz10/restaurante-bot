## path1
* greet
  - utter_greet
* order
  - dish_form
  - form{"name": "dish_form"}
  - form{"name": null}
  - action_show_orders
  - utter_anything_else
* deny
  - utter_please_wait
* thankyou
  - utter_noworries
* request_bill
  - action_show_orders
  - utter_sending_bill
* goodbye
  - utter_goodbye


## interactive_story_1
* greet
    - utter_greet
* order{"number": 1, "dish": "Big Mac"}
    - slot{"dish": "Big Mac"}
    - slot{"number": 1}
    - dish_form
    - form{"name": "dish_form"}
    - slot{"dish": "Big Mac"}
    - slot{"number": 1}
    - slot{"dish": "Big Mac"}
    - slot{"number": 1}
    - slot{"requested_slot": "drink"}
* form: order{"number": 1, "drink": "COCA COLA"}
    - slot{"drink": "COCA COLA"}
    - slot{"number": 1}
    - form: dish_form
    - slot{"number": 1}
    - slot{"drink": "COCA COLA"}
    - slot{"requested_slot": "observation"}
* form: deny
    - form: dish_form
    - slot{"observation": "Nenhuma observação"}
    - slot{"requested_slot": "confirmed"}
* form: affirm{"confirmed": true}
    - slot{"confirmed": true}
    - form: dish_form
    - slot{"confirmed": true}
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_show_orders
    - utter_anything_else
* just_that
    - utter_please_wait
* thankyou
    - utter_noworries
* request_bill
    - action_show_orders
    - utter_sending_bill
* goodbye
    - utter_goodbye
