from flask import Flask, request
from random import randint

app = Flask(__name__)

winning = randint(1,100)

@app.route('/', methods=["GET", "POST"])
def guessing_game():
    if request.method == "POST":
       usernm = int(request.form["usernm"])
       if usernm == winning:
        return "Congratulations, you made it!"
       while usernm != winning:
           if usernm > winning:
               return """
                Too many, try again!"
                        <h1> Form - enter your guess</h1>
                <form method="POST" action="/">
                    <input type="number" name="usernm" placeholder="Try to guess:" required>
                    <input type="submit" value="Submit">
                """
           else:
               return """
                Too little!
                    <h1> Form - enter your guess</h1>
                    <form method="POST" action="/">
                        <input type="number" name="usernm" placeholder="Try to guess:" required>
                        <input type="submit" value="Submit">
                """
    elif request.method == "GET":
        return """
    <!doctype html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport">
            <title> Formular </title>
        </head>
        <body>
            <h1> Form - enter your guess</h1>
            <form method="POST" action="/">
                <input type="number" name="usernm" placeholder="Enter a number from 1 to 100" required>
                <input type="submit" value="Submit">
            <br><br>
        </body>
        </html>
                """


if __name__ == "__main__":
    app.run(debug = True)