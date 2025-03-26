from flask import Flask, request, render_template
from psycopg2 import OperationalError

from exercise1 import execute_query_on_database


app = Flask(__name__)

# Endpoint get na zobrazeni + editace

# Endpoint post na update filmu

update_query = """
UPDATE movies
    SET
        name='test11',
        description='test11'
    WHERE id = 10
;
"""

@app.route("/movie/<movie_id>", methods=["GET", "POST"])
def update_movie(movie_id):
    try:
        
        try:
            movie_id = int(movie_id)
        except ValueError as e:
            return f"Invalid ID. Error: {e}."
        
        if request.method == "GET":
            
            query = f"SELECT id, name, description FROM movies WHERE id = {movie_id};"
            
            try:
                movie_data = execute_query_on_database(
                    database_name="cinemas_db",
                    sql_query=query
                )
                
                if movie_data is not None:
                    # movie_id = movie_data[0][0]
                    # movie_name = movie_data[0][1]
                    # movie_description = movie_data[0][2]
                    # movie_rating = movie_data[0][3]
                    movie_id, movie_name, movie_description = movie_data[0]
                else:
                    return "There is no such movie!"

                return render_template(
                    "form.html",
                    movie_id=movie_id,
                    movie_name=movie_name,
                    movie_description=movie_description
                )
            
            except OperationalError as e:
                err_msg = f"Encountered psql oper. error: {e}"
                print(err_msg)
                return err_msg
            
        if request.method == "POST":

            movie_name = request.form["movie_name"]
            movie_description = request.form["movie_description"]
            query = f"""
            UPDATE movies 
                SET
                    name='{movie_name}',
                    description='{movie_description}'
                WHERE id = {movie_id}
            ;
            """
            try:
                execute_query_on_database(
                    database_name="cinemas_db",
                    sql_query=query
                )
                return "Changed movie data",
            except OperationalError as e:
                err_msg = f"Encountered psql oper. error: {e}"
                print(err_msg)
                return err_msg
    
    except Exception as ex:
        return f"Encountered error: {ex}"


if __name__=="__main__":
    app.run(debug=True)

