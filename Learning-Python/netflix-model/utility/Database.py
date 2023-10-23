from pymongo import MongoClient


class Database:
    INSTANCE = None

    def __new__(cls):
        if cls.INSTANCE is None:
            cls.INSTANCE = super(Database, cls).__new__(cls)
            cls.INSTANCE.initialize()
        return cls.INSTANCE

    def initialize(self):
        self.mongo_client = None

        HOST = "localhost"
        PORT = 27017
        DATABASE_NAME = "netflix"

        try:
            self.mongo_client = MongoClient(HOST, PORT)
            self.mongo_client.get_database(DATABASE_NAME)
        except Exception as e:
            print(e)

    def get_netflix_database(self):
        return self.mongo_client.get_database("netflix")
