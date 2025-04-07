from flask import Flask
from flask import render_template
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def home():
    year = datetime.now().year
    print(year)
    return render_template('index.html', year=year)

if __name__ == "__main__":
    app.run(debug=True)
