from flask import Flask
from datetime import datetime

app = Flask(__name__)

@app.route("/time")
def show_current_time():
    return str(datetime.now()) + "|||" + str(datetime.today())

#.strftime('%a %d %b %Y, %I:%M%p')


if __name__=="__main__":
    app.run(debug=True)

