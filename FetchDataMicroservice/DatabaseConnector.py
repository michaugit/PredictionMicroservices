import psycopg2
import json


class SingletonMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class DatabaseConnector(metaclass=SingletonMeta):
    config = None
    conn = None

    def __init__(self):
        self.__import_config()
        self.__connect()

    def __del__(self):
        self.__disconnect()

    def __import_config(self):
        with open('sql/config.json') as json_file:
            self.config = json.load(json_file)

    def __connect(self):
        try:
            self.conn = psycopg2.connect(database=self.config['dbName'], user=self.config['dbUser'],
                                         password=self.config['dbPass'], host="127.0.0.1", port="5432")
            print("Database opened successfully")
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)

    def __disconnect(self):
        if self.conn is not None:
            self.conn.close()
            print('Database connection closed.')

    def execute_select(self, query: str):
        data = None
        if self.conn:
            cursor = self.conn.cursor()
            cursor.execute(query)
            data = cursor.fetchall()
        else:
            print("No connection to Database.")

        return data

    def execute_insert(self, query: str):
        if self.conn:
            cursor = self.conn.cursor()
            cursor.execute(query)
            self.conn.commit()
        else:
            print("No connection to Database.")
