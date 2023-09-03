# Import necessary libraries
from textbase import bot, Message
import openai
from typing import List
import time

# Load your OpenAI API key
openai.api_key = ""

# Define the system prompt with a travel theme
SYSTEM_PROMPT = "Welcome to TravelBot, your travel recommendation companion! Where would you like to go next?"

@bot()
def on_message(message_history: List[Message], state: dict = None):

    # Extract the user's message from the latest message in history
    user_message = message_history[-1]['content']

    # Initialize the response using the OpenAI API
    bot_response = generate_travel_response(user_message)

    response = {
        "data": {
            "messages": [
                {
                    "data_type": "STRING",
                    "value": bot_response
                }
            ],
            "state": state
        },
        "errors": [
            {
                "message": ""
            }
        ]
    }

    return {
        "status_code": 200,
        "response": response
    }

def generate_travel_response(user_message):
    # Generate a travel-related response using the OpenAI API
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=f"{SYSTEM_PROMPT}\nUser: {user_message}\nBot:",
        max_tokens=100  # You can adjust the response length as needed
    )

    return response.choices[0].text

if __name__ == "__main__":
    print("TravelBot: Hello! I'm here to help you plan your next adventure.")

    # Loop to provide automatic responses every 5 seconds
    while True:
        user_input = input("You: ")
        
        if user_input.lower() in ["exit", "quit", "goodbye"]:
            print("TravelBot: Goodbye! Have a fantastic trip!")
            break