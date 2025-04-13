
import psycopg2

import os

class DocumentCache:
    _cache = {}
    def __init__(self):
        self.sql = None
        self.conx = psycopg2.connect(
            dbname="cinemas_db",
            username='postgres',
            password=os.environ['POSTGRES_PASSWORD'],
            host="localhost",
            port="5432"
        )
        self.set_sql()

    def get(self, key):
        if key in self._cache:
            return self._cache[key]
        else:
            return self.find_document_version(key)
        
    def set_sql(self, sql: None):
        if sql is None:
            sql = """
            SELECT *
            FROM document_envelopes
            WHERE version  == %s
            """
        self.sql = sql
        
    def find_document_version(self, key):
        # Volani databaze
        if self.sql is None:
            raise ValueError("SQL query is not set")
        
        with self.conx:
            with self.conx.cursor() as cursor:
                doc_envelope = cursor.execute(self.sql, (key,))
                self.conx.commit()

        if doc_envelope:
            return doc_envelope
        return None
    

class GenericCache:
    def __init__(self):
        self._cache = {}
    def add_key_value_pair(self, key, value):
        self._cache[key] = value


cache = {}
vstupni_data = [1,2,3,4,5,1,2]

for datovy_bod in vstupni_data:
    if not datovy_bod in cache:
        vystupni_data = funkce(vstupni_data)
        cache[datovy_bod] = vystupni_data
    else:
        vystupni_data = cache[datovy_bod]
