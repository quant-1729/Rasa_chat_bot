from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import requests
import json

class FallbackAction(Action):
    def name(self) -> Text:
        return "action_fallback"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict[Text, Any]]:
        headers = {
            "Authorization": "2d27f32efc3f4c708d070021deb61f1b",
            "Content-Type": "application/json",
            # Add any other headers as needed
        }

        # Your API URL
        api_url = "https://api.bing.microsoft.com/"

        # Make an API request
        response = requests.get(api_url)

        if response.status_code == 200:
            # Extract the API response
            api_response = response.json()

            # Customize the response as needed
            message = api_response.get("message", "Fallback response")

            # Send the API response as a message to the user
            dispatcher.utter_message(text=message)
        else:
            dispatcher.utter_message(text="Sorry, I couldn't find an answer.")

        return []
