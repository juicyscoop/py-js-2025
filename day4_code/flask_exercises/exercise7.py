from flask import Flask, request

app = Flask(__name__)

@app.route("/", methods=["POST", "GET"])
def hello():
    if request.method == "POST":
        name = request.form["jmeno"]
        return f"Ahoj {name}"
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
                    <h1> Form - enter your name </h1>
                    <form method="POST" action="/">
                        <input type="text" name="jmeno" placeholder="Enter your name here" required>
                        <input type="submit" value="Submit">
                    <br><br>
                    </form>
                </body>
                </html>
            """


if __name__=="__main__":
    app.run(debug=True)


