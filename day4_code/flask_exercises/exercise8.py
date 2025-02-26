from flask import Flask, request

app = Flask(__name__)


@app.route("/", methods=["POST", "GET"])
def calculator():
    # Validace Libor
    """
    try:
        cislo1 = float(request.form['cislo1'])
        cislo2 = float(request.form['cislo2'])
        operace = request.form['operace']
        if operace == '/' and cislo2 == 0:
            raise ZeroDivisionError('Dělení nulou není povoleno!')
    except ZeroDivisionError as e:
        return str(e)

    except ValueError:
        return 'Neplatný vstup!'
    """

    if request.method == "POST":
        # Kontrola vstupu
        try:
            cislo1 = int(request.form["cislo1"])
        except ValueError:
            return "Cislo 1 was not a number!"

        try:
            cislo2 = int(request.form["cislo2"])
        except ValueError:
            return "Cislo 2 was not a number!"

        operace = request.form["operace"]

        if operace == ":" and cislo2 == 0:
            return "Cannot divide by 0!"

        # Vykon kalkulace
        if operace == "+":
            return str(cislo1 + cislo2)
        elif operace == "-":
            return str(cislo1 - cislo2)
        elif operace == "*":
            return str(cislo1 * cislo2)
        else:
            return str(cislo1 / cislo2)

    # Zobrazeni formulare
    elif request.method == "GET":
        options_string = "\n".join(
            [
                f"""<option value="{val}">{name}</option>"""
                for val, name in
                    [("*", "Nasobeni"), ("+", "Scitani"),  ("-", "Odcitani"), (":", "Deleni")]
            ]
        )
        return f"""
            <!doctype html>
                <html lang="en">
                <head>
                    <meta charset="UTF-8">
                    <meta name="viewport">
                    <title> Formular - operace nad cisly </title>
                </head>
                <body>
                    <h1> Form - enter two numbers, select operation </h1>
                    <form method="POST" action="/">
                        <input type="number" name="cislo1" placeholder="Enter first number here" required>
                        <input type="number" name="cislo2" placeholder="Enter second number here" required>
                        <select name="operace">
                            {options_string}
                        </select>
                        <input type="submit" value="Submit">
                    <br><br>
                    </form>
                </body>
                </html>
            """


if __name__=="__main__":
    app.run(debug=True)


