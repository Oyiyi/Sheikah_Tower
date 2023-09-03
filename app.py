import logging
import threading
from flask import Flask, request
from wrapper import ChatApi
from collections import deque

app = Flask(__name__)

logging.basicConfig(filename='app.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
chatapi = ChatApi()

messages = deque()
def run_chat_api(user_message):
    bot_response = chatapi.chat_api(user_message)
    messages.append(('Bot', bot_response))
    logging.info(f'Bot response: {bot_response}')

@app.route('/')
def chat():
    chat_history = ""
    for sender, message in messages:
        chat_history += f"<p><strong>{sender}:</strong> {message}</p>"
    return f"""
        <html>
        <head>
            <title>Chat Page</title>
        </head>
        <body>
            <h1>Chat Page</h1>
            <div id="chatbox">
                {chat_history}
            </div>
            <form action="/send" method="post">
                <input type="text" name="message" placeholder="Enter your message">
                <button type="submit">Send</button>
            </form>
        </body>
        </html>
    """

@app.route('/send', methods=['POST'])
def send_message():
    user_message = request.form.get('message')
    messages.append(('You', user_message))
    logging.info(f'User sent message: {user_message}')
    thread = threading.Thread(target=run_chat_api, args=(user_message,))
    thread.start()
    return chat()

if __name__ == '__main__':
    app.run(debug=True)
