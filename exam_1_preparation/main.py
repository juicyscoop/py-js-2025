
from psycopg2 import connect

import logging
logging.basicConfig(level=logging.DEBUG)
#logging.BASIC_FORMAT = "%(asctime)s %(levelname)s %(message)s"
from psycopg2.errors import DuplicateDatabase


def execute_query_on_database(database_name: str, sql_query: str) -> list | None:
    # database na vstupu
    # query na vstupu
    cnx = connect(
        user="postgres",
        dbname=database_name,
        password='heslo',
        host="localhost",
        port="5432"
    )
    cnx.autocommit = True
    cursor = cnx.cursor()
    
    cursor.execute(sql_query)

    vystup = []
    if "SELECT" in sql_query or "select" in sql_query:
        for i in cursor:
            vystup.append(i)
    
    cnx.commit()

    cursor.close()
    cnx.close()

    return vystup or None


def handle_db_init():
    sql1 = """
    CREATE DATABASE test_retry;
    """

    try:
        res = execute_query_on_database("postgres", sql1)
        logging.info("res: ", res)
        # V tuhle chvili je databaze vytvorena
    except DuplicateDatabase as dd_err:
        logging.error(f"Encountered error (db already exists): {dd_err}")


if __name__ == "__main__":
    handle_db_init()