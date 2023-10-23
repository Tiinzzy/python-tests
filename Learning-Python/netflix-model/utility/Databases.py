from pymongo import MongoClient

HOST = "localhost"
PORT = 27017
NETFLIX_DB = "netflix"
PRIME_DB = "prime"


class Database:
    mongo_client = None

    @staticmethod
    def get_netflix_database():
        if Database.mongo_client is None:
            Database.mongo_client = MongoClient(HOST, PORT)
        return Database.mongo_client.get_database(NETFLIX_DB)

    @staticmethod
    def get_prime_database():
        if Database.mongo_client is None:
            Database.mongo_client = MongoClient(HOST, PORT)
        return Database.mongo_client.get_database(PRIME_DB)


class Databases:
    NETFLIX = Database.get_netflix_database()
    PRIME = Database.get_prime_database()
