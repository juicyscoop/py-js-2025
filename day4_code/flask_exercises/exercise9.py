from flask import Flask, request
from random import randint

app = Flask(__name__)

winning_guess = randint(1, 100)

template = """
        <!doctype html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport">
            <title> Guessing Game </title>
        </head>
        <body>
            <h1> Guessing Game </h1>
            <form method="POST" action="/">
                <input type="text" name="guessed_number" placeholder="Enter your guess here" required>
                <input type="submit" value="Submit">
            <br><br>
            </form>
        </body>
        </html>
"""

@app.route("/", methods=["GET"])
def guessing_game_get():
    global winning_guess
    print("Correct guess:", winning_guess)
    return template

@app.route("/", methods=["POST"])
def guessing_game_post():
    global winning_guess
    guess_from_user = int(request.form['guessed_number'])
    if winning_guess is not None:
        if guess_from_user < winning_guess:
            return "Too little!" + template
        if guess_from_user > winning_guess:
            return "Too much!" + template
        if guess_from_user == winning_guess:
            #return "Congratulations, you made it!"
            winning_guess = randint(1, 10)
            print("NEW CORRECT GUESS: ", winning_guess)
            return "Congratulations, you made it! || NEW GAME: " + template
    else:
        return "Need a valid number!"


if __name__=="__main__":
    app.run(debug=True)


