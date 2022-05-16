from flask import Flask
import random
app = Flask(__name__)


random_number = random.randrange(0, 9)
print(random_number)


@app.route('/')
def guess_number():
    return '<h1 style="text-align: center">Guess a number between 0 and 9!</h1>' \
           '<iframe src="https://giphy.com/embed/13RcbHeXlLNysE" width="480" height="304" frameBorder="0" ' \
           'class="giphy-embed" allowFullScreen></iframe><p><a href="https://giphy.com/gifs/' \
           'i-love-lucy-lucille-ball-13RcbHeXlLNysE">via GIPHY</a></p>'


@app.route('/<int:guess>')
def answer(guess):
    if guess == random_number:
        return '<h1 style="color:green">You found me!</h1>'
    elif guess > random_number:
        return '<h1 style="color:blue">Too high!</h1>' \
               '<iframe src="https://giphy.com/embed/wHB67Zkr63UP7RWJsj" width="480" height="337" frameBorder="0" class="giphy-embed" allowFullScreen></iframe><p><a href="https://giphy.com/gifs/wHB67Zkr63UP7RWJsj">via GIPHY</a></p>'
    else:
        return '<h1 style="color:red">Too low!</h1>' \
               '<iframe src="https://giphy.com/embed/2uI9astifwiSUWVOTT" width="480" height="270" frameBorder="0" class="giphy-embed" allowFullScreen></iframe><p><a href="https://giphy.com/gifs/greatbigstory-dance-omg-2uI9astifwiSUWVOTT">via GIPHY</a></p>'


if __name__ == "__main__":
    app.run(debug=True)
