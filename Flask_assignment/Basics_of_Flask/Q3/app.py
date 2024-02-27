#3. Develop a Flask app that uses URL parameters to display dynamic content.

from flask import Flask ,request ,render_template
app = Flask(__name__)

@app.route("/")
def dynamic_content():
    return (
        "<h1>Welcome to the dynamic Page!</h1>"
        "<p>To access dynamic content, go to <a href='/greet?name=YourName'>/greet?name='YourName'></a></p>"
    )
    
@app.route("/greet")
def greet():
    data = request.args.get("name")
    if data :
        return f"Hello {data}"
    else:
        return f"Hello anonymous"
 
if __name__ == "__main__" :
    app.run(debug = True)