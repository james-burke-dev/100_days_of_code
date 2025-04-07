from flask import Flask
from flask import render_template
from datetime import datetime
import requests

AGIFY_API = "https://api.agify.io?name="
GENDERIZE_API = "https://api.genderize.io?name="

app = Flask(__name__)

def get_age(name):
    url = AGIFY_API + name
    response = requests.get(url=url)
    age = response.json()['age']
    return age

def get_gender(name):
    url = GENDERIZE_API + name
    response = requests.get(url=url)
    gender = response.json()['gender']
    return gender

@app.route('/')
def home():
    year = datetime.now().year
    print(year)
    return render_template('index.html', year=year)

@app.route('/guess/<name>')
def guess(name):
    gender = get_gender(name)
    age = get_age(name)
    return render_template('guess.html', name=name, age=age, gender=gender)

if __name__ == "__main__":
    app.run(debug=True)
