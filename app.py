from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, boys and girls come listen the show!"
