
from flask import Flask
from utils import convert_int_to_float

app = Flask(__name__)


@app.route("/hello")
def hello():
    vystupni = convert_int_to_float(10)
    print("vystupni:",vystupni)
    return "Hello user!"


if __name__=="__main__":
    app.run(debug=True)
