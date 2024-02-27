# 10. Design a Flask app with proper error handling for 404 and 500 errors.
from flask import Flask, render_template

app = Flask(__name__)

# Error handler for 404 Not Found error
@app.errorhandler(404)
def not_found_error(error):
    return render_template('404.html'), 404

# Error handler for 500 Internal Server Error
@app.errorhandler(500)
def internal_server_error(error):
    return render_template('500.html'), 500

# Sample route for testing
@app.route('/')
def index():
    # Simulate an error for testing
    # Uncomment the line below to trigger a 500 Internal Server Error
    #1 / 0
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)

