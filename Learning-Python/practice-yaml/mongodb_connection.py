from pymongo import MongoClient


class MongodbConnection:
    def __init__(self, host_name, port_name):
        self.mongo_host = host_name
        self.mongo_port = port_name
        self.mongo_client = None

    def connect(self):
        server_info = None
        try:
            self.mongo_client = MongoClient(self.mongo_host, self.mongo_port)
            server_info = self.mongo_client.server_info()
        except Exception as e:
            print(e)
        return server_info is not None

    def disconnect(self):
        self.mongo_client.close()

    def insert(self, database_name, collection_name, documents):
        my_database = self.mongo_client[database_name]
        collection = my_database.get_collection(collection_name)
        collection.insert_many(documents)
