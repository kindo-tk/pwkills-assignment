#  12. Build a Flask app that updates data in real-time using WebSocket connections.
from flask import Flask, render_template
from flask_socketio import SocketIO

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key_here'
socketio = SocketIO(app)

# Data to be updated in real-time
data = {'counter': 0}

@app.route('/')
def index():
    return render_template('index.html', data=data)

@socketio.on('update_data')
def handle_update_data(new_data):
    global data
    data = new_data
    socketio.emit('data_updated', new_data)  # Remove broadcast=True

if __name__ == '__main__':
    socketio.run(app, debug=True)
