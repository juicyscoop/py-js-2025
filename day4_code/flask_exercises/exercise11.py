from flask import Flask, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def hello():
    if request.method == "POST":
        name = request.form["jmeno"]
        surname = request.form["prijmeni"]
        return f"Dobry den {name} {surname}"
    # prisel request metody GET
    return """
    <html>
        <head>
        </head>
        <body>
            <form>
                <input type="text" placeholder="Jmeno" name="jmeno">
                <input type="text" placeholder="Prijmeni" name="prijmeni">
                <button type="submit"> Send </button>
            </form>
        </body>
    </html>
    """



if __name__=="__main__":
    app.run(debug=True)


