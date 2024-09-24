from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/calculator')
def calculator():
    return render_template('calculator.html')

@app.route("/")
def index():
    return "Welcome to COMP3900 and COMP9900!"

if __name__ == '__main__':
    app.run(debug=True)
