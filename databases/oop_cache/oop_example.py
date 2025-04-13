import psycopg2
import os
import datetime

import json

class PostgresClient:
    def __init__(self):
        self.conx = psycopg2.connect(
            dbname="cinemas_db",
            user='postgres',
            password=os.environ['POSTGRES_PASSWORD'],
            host="localhost",
            port="5432",
            # stream=True
        )

    def execute_query_on_database(self, sql_query: str) -> list | None:
        cursor = self.conx.cursor()

        yield from cursor.execute(sql_query, stream=True)
        # 
        # vystup = []
        # if "SELECT" in sql_query or "select" in sql_query:
        #     for i in cursor:
        #         vystup.append(i)
        
        # self.conx.commit()
        # cursor.close()
        
        # yield vystup

class UserAnalyzer(PostgresClient):
    
    _cache = {}

    def __init__(self, config):
        super().__init__()
        self.config = config
        self.instance_time = datetime.datetime.now()
        self.user_column_name = None

    def aggregate_users(self):
        # users_data = self.execute_query_on_database(
        #     sql_query="""
        #     SELECT * FROM users
        #     """
        # )

        users_data = [1, 2, 3, 4, 5] # Dummy

        powered = [i**2 for i in users_data]

        print(f"powered made with list-comp.: {powered}, {type(powered)}")

        powered = (i**2 for i in users_data)

        print(f"powered made with generator-comp.: {powered} {type(powered)}")

    @staticmethod
    def convert_account_creation_time_to_human_readable(account_creation_time):
        return datetime.datetime.fromtimestamp(account_creation_time).strftime("%B %d, %Y")
    
    @staticmethod
    def list_products():
        # jakej typ produktu?
        # product_type = config["product_type"]
        products = {
            "fruit": ["apple", "banana", "orange", "plum"],
            "vegetables": ["potato", "carrot", "tomato", "cabbage"],
        }
        # yield from products[product_type]

    @classmethod
    def from_json(cls, json_filename):
        parsed_data = json.load(json_filename)
        # cls -> UserAnalyzer
        # parsed_data -> dict
        # cls(parsed_data)
        # UserAnalyzer(dict)
        return cls(parsed_data)

    @property
    def user_column_name(self):
        return self.user_column_name

    @user_column_name.setter
    def get_user_column_name(self, value):
        # validaci hodnoty
        self.user_column_name = value
    
    @user_column_name.deleter
    def delete_user_column_name(self):
        # validaci ze mazeme to co chceme
        del self.user_column_name


ua = UserAnalyzer(config = {"product_type": "fruit"})
ua = UserAnalyzer.from_json(json_filename="config.json")


ua.user_column_name = "user_id"
del ua.user_column_name



# staticmethod
# classmethod
# property


ua = UserAnalyzer()
human_readable_ts = ua.convert_account_creation_time_to_human_readable(unix_ts)

unix_ts = datetime.datetime.now().timestamp()

human_readable_ts = UserAnalyzer.convert_account_creation_time_to_human_readable(unix_ts)


key = "test"
cache_value = UserAnalyzer._cache[key]