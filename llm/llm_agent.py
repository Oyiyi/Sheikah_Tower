#below imports in main.py already
import openai
#openai.api_key = OPENAI_API_KEY

class Conversation:
    def __init__(self):
        # Historical message storage for the entire conversation todo can't keep adding messages, but how to fix it? Maybe summarize every 5 messages?
        # Main prompt here
        self.messages = [{"role": "system", "content": "Act as a tour guide in an Egyptian museum. Your name is Alice."},{"role": "assistant", "content": "Hi I'm Alice, your tour guide today! Ready to explore?"}]
        #print("\n\nVIP Guide: Hi I'm Alice, your tour guide today! Ready to explore?'")

    def call_api(self):
        # text + user inputs as inputs of calling LLM APIs
        response = openai.ChatCompletion.create(
            model='gpt-3.5-turbo',
            messages=self.messages,
            max_tokens=200,
            temperature=0.4  # More parameters can be added if necessary
            # presence_penalty=0, frequency_penalty=0 # [-2~2]
        )

        # Get response from calling the API
        completion = response['choices']
        message = completion[-1]['message']['content']
        return message
        # TODO: Add logic to calculate tokens used and speed
   
    def rolling_convo(self, user_input, found_db_texts=None, found_db_user_data=None):
        self.messages.append({"role": "user", "content": user_input})

        if found_db_texts is not None:
            self.messages.append({"role": "system", "content": f"Some helpful knowledge: {found_db_texts}"})

        if found_db_user_data is not None:
            self.messages.append({"role": "system", "content": f"Something you know about the user: {found_db_user_data}"})

        chat_response = self.call_api() # use new added user_input to call API again
        #print(f"\n\nVIP Guide: {chat_response}")
        self.messages.append({"role": "assistant", "content": chat_response}) #['system', 'assistant', 'user', 'function']
        return chat_response