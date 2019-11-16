## greet
* greet
  - utter_greet

## happy path
* greet
  - utter_greet
* ask_tea
  - tea_form
  - form{"name": "tea_form"}
  - form{"name": null}
  - utter_slots_values
* thankyou
  - utter_noworries

## direct
* ask_tea
  - tea_form
  - form{"name": "tea_form"}
  - form{"name": null}
  - utter_slots_values


## direct02
* ask_tea
  - tea_form
  - form{"name": "tea_form"}
  - form{"name": null}
  - utter_slots_values
* thankyou
  - utter_noworries

## sad path 1
* greet
  - utter_greet
* mood_unhappy
  - utter_cheer_up
  - utter_did_that_help
* affirm
  - utter_happy

## sad path 2
* greet
  - utter_greet
* mood_unhappy
  - utter_cheer_up
  - utter_did_that_help
* deny
  - utter_goodbye

## say goodbye
* goodbye
  - utter_goodbye
