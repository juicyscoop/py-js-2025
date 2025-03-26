from flask import Flask, request, render_template

from exercise1 import execute_query_on_database

app = Flask(__name__)

@app.route("/", methods=["POST", "GET"])
def add_movie():

    if request.method == "GET":
        return render_template('form.html')

    if request.method == "POST":
        # movie_name, movie_description, movie rating
        #     movie_name = str(request.form["movie_name"])
        #     movie_description = str(request.form["movie_description"])
        #     movie_rating = float(request.form["movie_rating"])

        try:
            product_name = str(request.form["movie_name"])
            product_description = str(request.form["movie_description"])
            product_rating = float(request.form["movie_rating"])

            query = f"""
            INSERT INTO products
            (name, description, rating)
            VALUES
            ('{product_name}', '{product_description}', {product_rating})
            ;
            """
            execute_query_on_database(
                database_name="exercises_db",
                sql_query=query
            )
            return "Success"
        except Exception as ex:
            return f"Encountered error: {ex}"


if __name__=="__main__":
    app.run(debug=True)

