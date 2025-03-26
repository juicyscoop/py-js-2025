from flask import Flask

from exercise1 import execute_query_on_database

app = Flask(__name__)

@app.route("/movie/<movie_id>")
def get_movie(movie_id):
    try:

        try:
            movie_id = int(movie_id)
        except ValueError as e:
            return f"Invalid ID. Error: {e}."

        query = f"SELECT * FROM movies WHERE id = {movie_id};"
        result = execute_query_on_database(
            database_name="cinemas_db",
            sql_query=query
        )
        
        return str(result)
    
    except Exception as ex:
        return f"Encountered error: {ex}"


if __name__=="__main__":
    app.run(debug=True)

