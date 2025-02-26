from flask import Flask

app = Flask(__name__)

@app.route("/count/<number1>/<number2>")
def summary(number1, number2):
    summ = float(number1) + float(number2)
    return str(summ)


if __name__=="__main__":
    app.run(debug=True)


