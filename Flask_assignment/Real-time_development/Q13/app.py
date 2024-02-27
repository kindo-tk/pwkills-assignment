# 13. Implement notifications in a Flask app using websockets to notify users of updates.

from flask import Flask, render_template
from flask_socketio import SocketIO

app = Flask(__name__)
app.config['SECRET_KEY'] = 'hulum'
socketio = SocketIO(app)

# Sample data to be updated
notifications = []

@app.route('/')
def index():
    return render_template('index.html', notifications=notifications)

@socketio.on('new_notification')
def handle_new_notification(notification):
    notifications.append(notification)
    socketio.emit('update_notifications', notifications, broadcast=True)

if __name__ == '__main__':
    socketio.run(app, debug=True)

