# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/

 from typing import Any, Text, Dict, List

 from rasa_sdk import Action, Tracker
 from rasa_sdk.executor import CollectingDispatcher


#class EnquireForm(Action):
#    def name(self) -> Text:
#      return "enquire_form"
    
#    @staticmethod
#    def required_slots(tracker: Tracker) -> List[Text]:
#    return ["email"]

#    def submit(
#        self,
#        dispatcher: CollectingDispatcher,
#        tracker: Tracker,
#        domain: Dict[Text, Any],
#    ) -> List[Dict]:
#        # Send email
#        return []

