from flask import Flask

from exercise1 import execute_query_on_database

app = Flask(__name__)

@app.route("/")
def list_products():
    result = execute_query_on_database(
        database_name="exercises_db",
        sql_query="select * from products;"
    )
    print(f"Products: {result}")
    return str(result)


if __name__=="__main__":
    app.run(debug=True)

