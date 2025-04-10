from flask import Flask
from flask import render_template
from flask import request
import requests

app = Flask(__name__)

@app.route('/')
def home(name=None):
    return render_template('index.html', name=name)

@app.route('/login', method=["POST"])
def login():
    name = request.form["username"]
    password = request.form["password"]

if __name__ == "__main__":
    app.run()
