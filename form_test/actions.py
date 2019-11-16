# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"

# from typing import Any, Text, Dict, List
#
# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher
#
#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message("Hello World!")
#
#         return []

from typing import Dict, Text, Any, List, Union, Optional
from rasa_sdk import Tracker
from rasa_sdk import Action
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.forms import FormAction


class TeaForm(FormAction):
    def name(self) -> Text:
        return "tea_form"

    @staticmethod
    def required_slots(tracker) -> List[Text]:
        return ["name", "size", "sweetness", "bubble", "number"]

    def slot_mappings(self) -> Dict[Text, Union[Dict, List[Dict]]]:

        return {
            "name": self.from_entity(entity="name", not_intent="chitchat"),
            "number": [
                self.from_entity(entity="number", intent=["ask_number", "ask_tea"]),
                self.from_entity(entity="number"),
            ],
            "bubble": [
                self.from_entity(entity="bubble"),
                self.from_intent(intent="affirm", value="加珍珠"),
                self.from_intent(intent="deny", value="不加珍珠"),
            ],
            "size": [
                self.from_entity(entity="size"),
            ],
            "sweetness": [
                self.from_entity(entity="sweetness"),
            ],
        }

    @staticmethod
    def name_db() -> List[Text]:
        return [
            "珍珠奶茶",
            "珍珠",
            "椰果奶茶",
            "椰果",
            "仙草奶茶",
            "仙草",
            "皇家奶茶",
            "皇家",
            "热可可",
            "热可可奶茶",
        ]

    @staticmethod
    def size_db() -> List[Text]:
        return [
            "大杯",
            "小杯",
            "中杯",
            "大",
            "中",
            "小",
        ]

    @staticmethod
    def is_int(string: Text) -> bool:
        """Check if a string is an integer"""

        try:
            int(string)
            return True
        except ValueError:
            return False

    def validate_name(
            self,
            value: Text,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any],
    ) -> Optional[Text]:

        if value in self.name_db():
            return {"name": value}
        else:
            dispatcher.utter_template("utter_wrong_name", tracker)
            return {"name": None}

    def validate_size(
            self,
            value: Text,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text,Any],
    ) -> Optional[Text]:

        if value in self.size_db():
            return {"size": value}
        else:
            dispatcher.utter_template("utter_wrong_size", tracker)
            return {"size": None}

    # def validate_number(
    #         self,
    #         value: Text,
    #         dispatcher: CollectingDispatcher,
    #         tracker: Tracker,
    #         domain: Dict[Text, Any],
    # ) -> Optional[Text]:
    #
    #     if self.is_int(value) and int(value) > 0:
    #         return {"number": value}
    #     else:
    #         dispatcher.utter_template("utter_wrong_number", tracker)
    #         return {"number": None}

    # def validate_bubble(
    #         self,
    #         value: Text,
    #         dispatcher: CollectingDispatcher,
    #         tracker: Tracker,
    #         domain: Dict[Text, Any],
    # ) -> Any:
    #     if isinstance(value, str):
    #         if "加" in value:
    #             return {"bubble": "加珍珠"}
    #         elif "不要" in value:
    #             return {"bubble": "不加珍珠"}
    #         else:
    #             dispatcher.utter_template("utter_wrong_bubble", tracker)
    #             return {"bubble": None}
    #     else:
    #         return {"bubble": value}

    def submit(self, dispatcher, tracker, domain):
        dispatcher.utter_template("utter_submit", tracker)
        return []


class ActionAskPlace(Action):

    def name(self) -> Text:
        return "action_ask_place"

    def run(self, dispatcher, tracker, domain):
        place = tracker.get_slot("place")
        if place is None:
            dispatcher.utter_message("请问您想要知道哪里？")
            return []
        if place == "厦门":
            dispatcher.utter_message("{}在福建".format(place))
        elif place == "泉州":
            dispatcher.utter_message("{}在福建".format(place))
        elif place == "樟树":
            dispatcher.utter_message("{}在江西".format(place))
            return []
