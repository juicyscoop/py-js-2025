from flask import Flask, request

app = Flask(__name__)

@app.route("/", methods=["POST", "GET"])
def get_or_post():
    if request.method == "POST":
        return "You have sent a POST request!"
    if request.method == "GET":
        return "You have sent a GET request!"


if __name__=="__main__":
    app.run(debug=True)


