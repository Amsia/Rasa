## interactive_story_1
* ask_place
    - action_ask_place
* ask_place
    - action_ask_place
* ask_place{"place": "泉州"}
    - slot{"place": "泉州"}
    - action_ask_place
* ask_place{"place": "厦门"}
    - slot{"place": "厦门"}
    - action_ask_place
* greet
    - utter_greet
* mood_great
    - utter_happy
* stop
    - utter_goodbye

## interactive_story_1
* greet
    - utter_greet
* ask_tea
    - tea_form
    - form{"name": "tea_form"}
    - slot{"requested_slot": "name"}
* form: inform{"name": "热可可"}
    - slot{"name": "热可可"}
    - form: tea_form
    - slot{"name": null}
    - slot{"requested_slot": "name"}
* form: inform{"name": "皇家奶茶"}
    - slot{"name": "皇家奶茶"}
    - form: tea_form
    - slot{"name": "皇家奶茶"}
    - slot{"requested_slot": "size"}
* form: inform{"size": "中杯"}
    - slot{"size": "中杯"}
    - form: tea_form
    - slot{"size": "中杯"}
    - slot{"requested_slot": "sweetness"}
* form: ask_tea{"sweetness": "两分甜"}
    - slot{"sweetness": "两分甜"}
    - form: tea_form
    - slot{"sweetness": "两分甜"}
    - slot{"requested_slot": "bubble"}
* form: deny
    - form: tea_form
    - slot{"bubble": false}
    - slot{"requested_slot": "number"}
* form: ask_tea{"size": "五杯"}
    - slot{"size": "五杯"}
    - form: tea_form
    - slot{"size": null}
    - slot{"requested_slot": "size"}
* form: inform{"size": "中杯"}
    - slot{"size": "中杯"}
    - form: tea_form
    - slot{"size": "中杯"}
    - slot{"requested_slot": "number"}
* form: inform{"number": "2"}
    - slot{"number": "2"}
    - form: tea_form
    - slot{"number": "2"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - utter_slots_values
* thankyou
    - utter_noworries

## Chat with me

* greet
    - action_default_fallback
* ask_tea
    - tea_form
    - form{"name":"tea_form"}
    - slot{"requested_slot":"name"}
* inform{"name":"椰果奶茶"}
    - slot{"name":"椰果奶茶"}
    - tea_form
    - slot{"name":"椰果奶茶"}
    - slot{"requested_slot":"size"}
* inform{"size":"大杯"}
    - slot{"size":"大杯"}
    - tea_form
    - slot{"size":"大杯"}
    - slot{"requested_slot":"sweetness"}
* stop
    - action_default_fallback
* mood_unhappy
    - action_default_fallback
* ask_tea
    - action_default_fallback
* ask_tea{"sweetness":"五分甜"}
    - slot{"sweetness":"五分甜"}
    - tea_form
    - slot{"sweetness":"五分甜"}
    - slot{"requested_slot":"bubble"}
* deny
    - tea_form
    - slot{"bubble":false}
    - slot{"requested_slot":"number"}
* inform{"number":"８"}
    - slot{"number":"８"}
    - tea_form
    - slot{"number":"８"}
    - form{"name":null}
    - slot{"requested_slot":null}
    - utter_slots_values
* ask_tea
    - action_default_fallback
