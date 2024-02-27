# 11. Create a real-time chat application using Flask-SocketIO

from flask import Flask, render_template
from flask_socketio import SocketIO

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key_here'
socketio = SocketIO(app)

# Store the usernames in a set
users = set()

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('message')
def handle_message(message):
    print('Received message: ' + message)
    socketio.emit('message', message)

@socketio.on('connect')
def handle_connect():
    print('Client connected')
    socketio.emit('user_count', len(users))

@socketio.on('disconnect')
def handle_disconnect():
    print('Client disconnected')
    socketio.emit('user_count', len(users))

@socketio.on('username')
def handle_username(username):
    users.add(username)
    socketio.emit('user_count', len(users))
    socketio.emit('message', f'{username} has joined the chat')

if __name__ == '__main__':
    socketio.run(app, debug=True)
