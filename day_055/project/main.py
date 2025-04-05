import random
from flask import Flask
app = Flask(__name__)

answer = random.randint(0,100)

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/<int:guess>')
def show_result(guess):
    if guess == answer:
        return '<h1 style="color:green">Correct!</h1>' \
        '<img src="https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fwww.levernews.com%2Fcontent%2Fimages%2F2021%2F05%2Fd65350badaede26fa1f3ecc1a589046b-2.gif&f=1&nofb=1&ipt=7d6c352156c9b0a433c558bad9040d3753d2a6c98a197d1a83dcfc208a8d63c0&ipo=images"'
    elif guess < answer:
        return '<h1 style="color:red">Too Low!</h1>' \
        '<img src="https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fmedia1.tenor.com%2Fm%2FfwX4w5mCyEQAAAAC%2Fits-too-low-egoraptor.gif&f=1&nofb=1&ipt=f1db83d5e785ecb74f16cf339257274d57a29ff81065f6f6c486722e94a0d6c7&ipo=images"'
    elif guess > answer:
        return '<h1 style="color:red">Too high!</h1>' \
        '<img src="https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fmedia.tenor.com%2Fp9Sor_DlVj8AAAAM%2Fthats-way-too-high-ollie.gif&f=1&nofb=1&ipt=e524687840b3434e242a01836a408f9df1eb782c46916e77f2a5a6280295771e&ipo=images"'
    else:
        return '<h1>Guess was not a number</h1>' \
        '<img src="https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fwww.levernews.com%2Fcontent%2Fimages%2F2021%2F05%2Fd65350badaede26fa1f3ecc1a589046b-2.gif&f=1&nofb=1&ipt=7d6c352156c9b0a433c558bad9040d3753d2a6c98a197d1a83dcfc208a8d63c0&ipo=images"'

if __name__ == "__main__":
    app.run(debug=True)
