# 8. Implement user authentication and registration in a Flask app using Flask-Login
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.secret_key = 'hulum'
# Configure Flask-Login
login_manager = LoginManager()
login_manager.init_app(app)

# Sample user data (replace with your database logic)
users = {
    'user1': {'username': 'user1', 'password_hash': generate_password_hash('password1')},
    'user2': {'username': 'user2', 'password_hash': generate_password_hash('password2')}
}

# User class for Flask-Login
class User(UserMixin):
    pass

@login_manager.user_loader
def load_user(username):
    if username in users:
        user = User()
        user.id = username
        return user
    return None

# Routes for authentication

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username in users and check_password_hash(users[username]['password_hash'], password):
            user = load_user(username)
            login_user(user)
            flash('Logged in successfully!', 'success')
            return redirect(url_for('index'))
        else:
            flash('Incorrect username or password', 'error')
    return render_template('login.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Logged out successfully!', 'success')
    return redirect(url_for('index'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username not in users:
            users[username] = {'username': username, 'password_hash': generate_password_hash(password)}
            flash('Registration successful! Please log in.', 'success')
            return redirect(url_for('login'))
        else:
            flash('Username already exists. Please choose a different one.', 'error')
    return render_template('register.html')

@app.route('/')
@login_required
def index():
    return render_template('index.html', username=current_user.id)

if __name__ == '__main__':
    app.run(debug=True)
