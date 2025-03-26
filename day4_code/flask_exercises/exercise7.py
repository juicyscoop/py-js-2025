from flask import Flask, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def hello():
    if request.method == "GET":
        return """
            <h1> Form - enter your name </h1>
            <form method="POST" action="/">
                <input type="text" name="jmeno" placeholder="Enter your name here" required>
                <input type="submit" value="Submit">
            <br><br>
            </form>
        """
    elif request.method == "POST":
        name = request.form["jmeno"]
        return f"Ahoj {name}"

if __name__=="__main__":
    app.run(debug=True)


