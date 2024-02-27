from flask import Flask, render_template

app = Flask(__name__)

@app.route('/',methods = ['GET', 'POST'])
def index():
    return render_template('index.html')

@app.route('/about.html',methods = ['GET', 'POST'])
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True)
