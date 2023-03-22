from flask import Flask
from random import randint

app = Flask(__name__)


@app.route("/")
def hello():
    return '<h1>Guess a number between 0 and 9</h1>' \
        '<img src="https://media.giphy.com/media/Cij37iSqbvzEpLgZmN/giphy.gif">'


@app.route("/<int:number>")
def check(number):
    random_num = randint(0, 10)
    if number == random_num:
        return '<h1 style="color: green">You found me!</h1>' \
            '<img src="https://media.giphy.com/media/xT0GqssRweIhlz209i/giphy.gif">'
    elif number > random_num:
        return '<h1 style="color: purple">Too high, try again!</h1>' \
            '<img src="https://media.giphy.com/media/3og0IuWMpDm2PdTL8s/giphy-downsized-large.gif">'
    elif number < random_num:
        return '<h1 style="color: red">Too low, try again!</h1>' \
            '<img src="https://media.giphy.com/media/LluZfzq5cmmFdZN3pi/giphy.gif">'


if __name__ == "__main__":
    app.run(debug=True)
