# Napsat funcki
# Na vstupu nazev databaze + sql query
# Na vystupu bude mit list(vysledku) (pro SELECT) a nebo None

from psycopg2 import connect


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


# Kod na otestovani

if __name__=="__main__":
    insert_query = """
    INSERT INTO movies
    (name, description, rating)
    VALUES
    ('Shrek', 'Fantasy movie.', 9)
    ;
    SELECT * FROM movies
    ;
    """
    filmy = execute_query_on_database(
        database_name="cinemas_db",
        sql_query=insert_query
    )
    print(f"Filmy: \n {filmy} \n")




