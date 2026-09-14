from google import genai
from dotenv import load_dotenv
import os
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key=api_key)

print("================================")
print("        Amol's AI Chatbot")
print("================================")
print("Type 'exit' to stop.\n")

previous_interaction_id = None

while True:

    user_message = input("You: ")

    if user_message.lower() == "exit":
        print("Bot: Goodbye! Have a great day!")
        break

    try:

        if previous_interaction_id is None:

            interaction = client.interactions.create(
                model="gemini-3.6-flash",
                input=user_message
            )

        else:

            interaction = client.interactions.create(
                model="gemini-3.6-flash",
                input=user_message,
                previous_interaction_id=previous_interaction_id
            )

        print("Bot:", interaction.output_text)
        print()

        
        previous_interaction_id = interaction.id

    except Exception as e:

        print("Error:", e)