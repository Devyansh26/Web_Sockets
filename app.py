from flask import Flask, render_template
from flask_socketio import SocketIO, send

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'

# Initialize SocketIO
socketio = SocketIO(app, cors_allowed_origins="*")

@app.route('/')
def index():
    return render_template('index.html')  # Loads the chat UI

# Handle messages from any user
@socketio.on('message')
def handle_message(msg):
    print(f'Received message: {msg}')
    send(msg, broadcast=True)  # Send the message to ALL connected clients

if __name__ == '__main__':
    socketio.run(app, debug=True)
