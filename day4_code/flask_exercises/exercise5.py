from flask import Flask
from random import randint

app = Flask(__name__)

LOWER_LIMIT = 1
UPPER_LIMIT = 1000

@app.route("/draw")
def draw_and_display():
    # Libor - [random.randint(0, 9) for _ in range(3)]
    return "<br>".join([str(randint(LOWER_LIMIT, UPPER_LIMIT)) for _ in range(3)])

# Vojtech
#def draw_display():
#    return f"{randint(0,9)} <br> {randint(0,9)} <br> {randint(0,9)}"

if __name__=="__main__":
    app.run(debug=True)


