#below imports in main.py already
import openai
#openai.api_key = OPENAI_API_KEY

class Conversation:
    def __init__(self):
        # Historical message storage for the entire conversation todo can't keep adding messages, but how to fix it? Maybe summarize every 5 messages?
        # Main prompt here
        self.messages = [{"role": "system", "content": "Act as a tour guide in an Egyptian museum."}]

    def call_api(self):
        # text + user inputs as inputs of calling LLM APIs
        response = openai.ChatCompletion.create(
            model='gpt-3.5-turbo',
            messages=self.messages,
            max_tokens=2000,
            temperature=0.4  # More parameters can be added if necessary
            # presence_penalty=0, frequency_penalty=0 # [-2~2]
        )

        # Get response from calling the API
        completion = response['choices']
        message = completion[-1]['message']['content']
        return message
        # TODO: Add logic to calculate tokens used and speed
   

    def start_rock(self):
        while True:
            # Add system message into prompt
            user_input = input("User: ")
            self.messages.append({"role": "user", "content": user_input})        
            chat_response = self.call_api()
            print(f"AI: {chat_response}")
            self.messages.append({"role": "AI", "content": chat_response})
