import logging
from flask import Flask, render_template_string
from collections import deque
from flask_socketio import SocketIO, emit
import eventlet
from wrapper import MECApp
eventlet.monkey_patch()

app = Flask(__name__)
socketio = SocketIO(app, logger=True, engineio_logger=True, cors_allowed_origins="*")

#socketio = SocketIO(app, cors_allowed_origins="*")

logging.basicConfig(filename='app.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

"""
class MECApp:
    def chat_api(self, msg):
        return "Echo: " + msg
"""
mec = MECApp()
messages = deque()

@app.route('/')
def chat():
    chat_history = "".join([f"<p><strong>{sender}:</strong> {message}</p>" for sender, message in messages])
    return render_template_string("""
        <html>
        <head>
        <title>Hello Link</title>
        <script src="https://cdnjs.cloudflare.com/ajax/libs/socket.io/4.0.1/socket.io.js"></script>
        <style>
            /* Use flexbox for layout */
            body {
                display: flex;
                flex-direction: column;
                height: 100vh;  /* Make the body fill the entire viewport height */
                margin: 0;
            }

            #chatbox {
                flex: 1;  /* Allow chatbox to grow and consume available space */
                overflow-y: auto;  /* Make chatbox scrollable */
                padding: 10px;
                border-bottom: 1px solid #ccc;
            }
        </style>
        </head>
        <body>
            <h1>Chat Page</h1>
            <div id="chatbox">
                {{ chat_history|safe }}
            </div>
            <form onsubmit="sendMessage(event)">
                <input type="text" name="message" id="messageInput" placeholder="Enter your message">
                <button type="submit">Send</button>
            </form>
            <script>
                var socket = io.connect('http://localhost:9090');
                
                socket.on('new message', function(data) {
                    var messageElement = document.createElement('p');
                    messageElement.innerHTML = '<strong>' + data.sender + ':</strong> ' + data.message;
                    var chatbox = document.getElementById('chatbox');
                    chatbox.appendChild(messageElement);
                    
                    // Scroll to the bottom of the chatbox
                    chatbox.scrollTop = chatbox.scrollHeight;
                });

                function sendMessage(event) {
                    event.preventDefault();
                    var inputElement = document.getElementById('messageInput');
                    var message = inputElement.value;
                    socket.emit('message sent', {'message': message});
                    inputElement.value = '';
                }
            </script>
        </body>
        </html>
    """, chat_history=chat_history)

@socketio.on('message sent')
def handle_message(data):
    user_message = data['message']
    messages.append(('You', user_message))
    logging.info(f'User sent message: {user_message}')
    emit('new message', {'sender': 'You', 'message': user_message}, broadcast=True)
    
    bot_response = mec.chat_api(user_message)
    logging.info(f'Bot response: {bot_response}')
    emit('new message', {'sender': 'Bot', 'message': bot_response}, broadcast=True)


if __name__ == '__main__':
    socketio.run(app, debug=True, port=9090)
