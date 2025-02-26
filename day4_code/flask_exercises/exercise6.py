from flask import Flask
from random import shuffle, randint, randrange

app = Flask(__name__)

@app.route("/lotto")
def lotto():
    s = list(range(1,50))
    shuffle(s)
    #s2 = randrange(6)
    #print(f"s2: {s2}")
    # "\n"
    # <br>
    return "<br>".join([str(i) for i in s[0:6]])

"""
def lotto(): # Vojtech
    final_seznam = []

    while len(final_seznam) < 6:
        new_random_number = randint(1,49)
        if new_random_number not in final_seznam:
            final_seznam.append(new_random_number)


    battery = list(range(50))
    for i in battery:
        battery.pop(i)
        battery.insert(i,randint(1,49))
    return "<br>".join([str(i) for i in battery[0:6]])
"""


if __name__=="__main__":
    app.run(debug=True)


