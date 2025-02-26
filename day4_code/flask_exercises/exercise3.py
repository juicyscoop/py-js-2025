from flask import Flask
from datetime import date

app = Flask(__name__)

@app.route("/")
def show_current_date():
    return date.today().strftime('%Y %m %d')


if __name__=="__main__":
    app.run(debug=True)


