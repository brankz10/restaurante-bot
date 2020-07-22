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
    - slot{"requested_slot": "note"}
* form: deny
    - form: dish_form
    - slot{"note": "Nenhuma observação"}
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

## interactive_story_1
* order{"number": 1, "dish": "CHEESEBURGER"}
    - slot{"dish": "CHEESEBURGER"}
    - slot{"number": 1}
    - dish_form
    - form{"name": "dish_form"}
    - slot{"dish": "CHEESEBURGER"}
    - slot{"number": 1}
    - slot{"dish": "CHEESEBURGER"}
    - slot{"number": 1}
    - slot{"requested_slot": "note"}
* form: note{"note": "sem maionese"}
    - slot{"note": "sem maionese"}
    - form: dish_form
    - slot{"note": "quero sem maionese"}
    - slot{"requested_slot": "confirmed"}
* form: deny{"confirmed": false}
    - slot{"confirmed": false}
    - form: dish_form
    - slot{"confirmed": false}
    - slot{"dish": null}
    - slot{"number": null}
    - slot{"note": null}
    - slot{"confirmed": null}
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_show_orders
    - utter_in_your_time
* thankyou
    - utter_noworries
* order{"dish": "CHEDDAR MCMELT"}
    - slot{"dish": "CHEDDAR MCMELT"}
    - dish_form
    - form{"name": "dish_form"}
    - slot{"dish": "CHEDDAR MCMELT"}
    - slot{"dish": "CHEDDAR MCMELT"}
    - slot{"requested_slot": "number"}
* form: inform{"number": 1}
    - slot{"number": 1}
    - form: dish_form
    - slot{"number": 1}
    - slot{"requested_slot": "note"}
* form: note{"note": "com muito cheddar"}
    - slot{"note": "com muito cheddar"}
    - form: dish_form
    - slot{"note": "sim, com muito cheddar"}
    - slot{"requested_slot": "confirmed"}
* form: affirm{"confirmed": true}
    - slot{"confirmed": true}
    - form: dish_form
    - slot{"confirmed": true}
    - slot{"dish": null}
    - slot{"number": null}
    - slot{"note": null}
    - slot{"confirmed": null}
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_show_orders
    - utter_anything_else
* affirm
    - utter_waiting_user_say
* order{"number": 1, "dish": "COCA COLA", "note": "sem gelo"}
    - slot{"dish": "COCA COLA"}
    - slot{"number": 1}
    - slot{"note": "sem gelo"}
    - dish_form
    - form{"name": "dish_form"}
    - slot{"dish": "COCA COLA"}
    - slot{"number": 1}
    - slot{"note": "sem gelo"}
    - slot{"dish": "COCA COLA"}
    - slot{"number": 1}
    - slot{"requested_slot": "confirmed"}
* form: affirm{"confirmed": true}
    - slot{"confirmed": true}
    - form: dish_form
    - slot{"confirmed": true}
    - slot{"dish": null}
    - slot{"number": null}
    - slot{"note": null}
    - slot{"confirmed": null}
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_show_orders
    - utter_anything_else
* just_that
    - utter_please_wait
* request_bill
    - action_show_orders
    - utter_sending_bill
* thankyou
    - utter_noworries
* goodbye
    - utter_goodbye

## interactive_story_1
* greet
    - utter_greet
* order{"number": 1, "dish": "MC CHICKEN"}
    - slot{"dish": "MC CHICKEN"}
    - slot{"number": 1}
    - dish_form
    - form{"name": "dish_form"}
    - slot{"dish": "MC CHICKEN"}
    - slot{"number": 1}
    - slot{"dish": "MC CHICKEN"}
    - slot{"number": 1}
    - slot{"requested_slot": "note"}
* form: note{"note": "sem queijo"}
    - slot{"note": "sem queijo"}
    - form: dish_form
    - slot{"note": "sim, quero sem queijo"}
    - slot{"requested_slot": "confirmed"}
* form: affirm{"confirmed": true}
    - slot{"confirmed": true}
    - form: dish_form
    - slot{"confirmed": true}
    - slot{"dish": null}
    - slot{"number": null}
    - slot{"note": null}
    - slot{"confirmed": null}
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_show_orders
    - utter_anything_else
* deny
    - utter_please_wait
* request_bill
    - action_show_orders
    - utter_sending_bill
* chitchat{"number": 1}
    - slot{"number": 1}
    - respond_chitchat
* goodbye
    - utter_goodbye

## interactive_story_1
* order{"dish": "DUPLO QUARTERAO"}
    - slot{"dish": "DUPLO QUARTERAO"}
    - dish_form
    - form{"name": "dish_form"}
    - slot{"dish": "DUPLO QUARTERAO"}
    - slot{"dish": "DUPLO QUARTERAO"}
    - slot{"requested_slot": "number"}
* form: inform{"number": 2}
    - slot{"number": 2}
    - form: dish_form
    - slot{"number": 2}
    - slot{"requested_slot": "note"}
* form: note{"note": "tire o picles"}
    - slot{"note": "tire o picles"}
    - form: dish_form
    - slot{"note": "quero que tire o picles"}
    - slot{"requested_slot": "confirmed"}
* form: affirm{"confirmed": true}
    - slot{"confirmed": true}
    - form: dish_form
    - slot{"confirmed": true}
    - slot{"dish": null}
    - slot{"number": null}
    - slot{"note": null}
    - slot{"confirmed": null}
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_show_orders
    - utter_anything_else
* deny
    - utter_please_wait
* chitchat
    - respond_chitchat
