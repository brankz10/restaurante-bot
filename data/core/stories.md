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
    - slot{"requested_slot": "observation"}
* form: observation{"observation": "sem maionese"}
    - slot{"observation": "sem maionese"}
    - form: dish_form
    - slot{"observation": "quero sem maionese"}
    - slot{"requested_slot": "confirmed"}
* form: deny{"confirmed": false}
    - slot{"confirmed": false}
    - form: dish_form
    - slot{"confirmed": false}
    - slot{"dish": null}
    - slot{"number": null}
    - slot{"observation": null}
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
* form: order{"number": 1}
    - slot{"number": 1}
    - form: dish_form
    - slot{"number": 1}
    - slot{"requested_slot": "observation"}
* form: observation{"observation": "com muito cheddar"}
    - slot{"observation": "com muito cheddar"}
    - form: dish_form
    - slot{"observation": "sim, com muito cheddar"}
    - slot{"requested_slot": "confirmed"}
* form: affirm{"confirmed": true}
    - slot{"confirmed": true}
    - form: dish_form
    - slot{"confirmed": true}
    - slot{"dish": null}
    - slot{"number": null}
    - slot{"observation": null}
    - slot{"confirmed": null}
    - form{"name": null}
    - slot{"requested_slot": null}
    - action_show_orders
    - utter_anything_else
* affirm
    - utter_waiting_user_say
* order{"number": 1, "dish": "COCA COLA", "observation": "sem gelo"}
    - slot{"dish": "COCA COLA"}
    - slot{"number": 1}
    - slot{"observation": "sem gelo"}
    - dish_form
    - form{"name": "dish_form"}
    - slot{"dish": "COCA COLA"}
    - slot{"number": 1}
    - slot{"observation": "sem gelo"}
    - slot{"dish": "COCA COLA"}
    - slot{"number": 1}
    - slot{"requested_slot": "confirmed"}
* form: affirm{"confirmed": true}
    - slot{"confirmed": true}
    - form: dish_form
    - slot{"confirmed": true}
    - slot{"dish": null}
    - slot{"number": null}
    - slot{"observation": null}
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
    - slot{"requested_slot": "observation"}
* form: observation{"observation": "sem queijo"}
    - slot{"observation": "sem queijo"}
    - form: dish_form
    - slot{"observation": "sim, quero sem queijo"}
    - slot{"requested_slot": "confirmed"}
* form: affirm{"confirmed": true}
    - slot{"confirmed": true}
    - form: dish_form
    - slot{"confirmed": true}
    - slot{"dish": null}
    - slot{"number": null}
    - slot{"observation": null}
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
