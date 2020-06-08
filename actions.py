# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

timezones = {
    "london": "UTC+1:00",
    "berlin":"UTC+2:00",
    "paris":"UTC+2:00",
    "milan":"UTC+2:00",
    "asia":"UTC+2:00",
    "australia":"UTC+8:00",
    "north america":"UTC+2:00",
    "colombia":"UTC-5:00",
    "france":"UTC+1:00",
    "germany":"UTC+1:00",
    "hong kong":"UTC+8:00",
    "iran":"UTC+3:30",
    "italy":"UTC+1:00",
    "india":"UTC+5:30"    
}

class ActionFindAndShowTimeZone(Action):

    def name(self) -> Text:
        return "action_show_time_zone"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        city = tracker.get_slot("city")

        timezone = timezones.get(city)

        if timezone is None:
            output = "Could not find the time zone for {}".format(city)
        else:
            output = "The time zone for {} is {}".format(city, timezone)

        dispatcher.utter_message(text=output)

        return [] 