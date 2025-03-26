from flask import Flask

from exercise1 import execute_query_on_database

app = Flask(__name__)

@app.route("/movies")
def list_movies():
    try:
        query = "SELECT * FROM movies;"
        result = execute_query_on_database(
            database_name="cinemas_db",
            sql_query=query
        )
        print(f"result: ", result)
        
        return "<br>".join(
            [
                "-- ".join(
                    [
                        str(i) for i in row
                    ]
                )
                for row in result
            ]
        )
    except Exception as ex:
        return f"Encountered error: {ex}"


if __name__=="__main__":
    app.run(debug=True)

