import eventlet
eventlet.monkey_patch()  # ✅ Must be the first import

from flask import Flask, render_template
from flask_socketio import SocketIO, send

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'

# Initialize Flask-SocketIO with eventlet
socketio = SocketIO(app, cors_allowed_origins="*", async_mode="eventlet")

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('message')
def handle_message(msg):
    print(f'Received message: {msg}')
    send(msg, broadcast=True)  # Send message to all connected clients

if __name__ == '__main__':
    # Use eventlet WSGI server
    socketio.run(app, host="0.0.0.0", port=5000, debug=True)
