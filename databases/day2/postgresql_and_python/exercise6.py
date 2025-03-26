from flask import Flask
from psycopg2 import OperationalError

from exercise1 import execute_query_on_database


app = Flask(__name__)

@app.route("/movie/<movie_id>")
def delete_movie(movie_id):
    try:

        try:
            movie_id = int(movie_id)
        except ValueError as e:
            return f"Invalid ID. Error: {e}."

        query = f"DELETE FROM movies WHERE id = {movie_id};"
        try:
            execute_query_on_database(
                database_name="cinemas_db",
                sql_query=query
            )
        except OperationalError as e:
            err_msg = f"Encountered psql oper. error: {e}"
            print(err_msg)
            return err_msg
        
        return "Success"
    
    except Exception as ex:
        return f"Encountered error: {ex}"


if __name__=="__main__":
    app.run(debug=True)

