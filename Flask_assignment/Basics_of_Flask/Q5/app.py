# 5. Implement user sessions in a Flask app to store and display user-specific data.

from flask import Flask, render_template, request, session, redirect, url_for

app = Flask(__name__)
app.secret_key = 'hulum'  # Set a secret key for session encryption

@app.route('/')
def index():
    if 'username' in session:
        username = session['username']
        return f"Hello, {username}! <a href='/logout'>Logout</a>"
    return 'You are not logged in. <a href="/login">Login</a>'

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        if username:
            session['username'] = username
            return redirect(url_for('index'))
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
