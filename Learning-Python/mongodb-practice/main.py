from pymongo import MongoClient
import json

MONGO_HOST = 'localhost'
MONGO_PORT = 27017


def get_connection():
    return MongoClient(MONGO_HOST, MONGO_PORT)


def test_get_databases():
    con = get_connection()
    databases = con.list_database_names()
    print(databases)
    con.close()


def test_show_collections(db_name):
    con = get_connection()
    my_db = con[db_name]
    collections = my_db.list_collection_names()
    print(collections)
    con.close()


def test_find_all_documents(db_name, collection_name, condition=None, return_fields=None):
    con = get_connection()
    my_db = con[db_name]
    collection = my_db.get_collection(collection_name)
    cursor = collection.find(condition, return_fields)
    print(len(list(cursor.clone())))
    for c in cursor:
        print(c)
    con.close()


def get_json_file():
    f = open('some_movies.json')
    data = json.load(f)
    return data


def test_insert_some_documents(db_name, collection_name):
    con = get_connection()
    my_db = con[db_name]
    collection = my_db.get_collection(collection_name)
    data = get_json_file()
    for d in data:
        collection.insert_one(d)
    con.close()


def test_drop_collection(db_name, collection_name):
    con = get_connection()
    my_db = con[db_name]
    collection = my_db.get_collection(collection_name)
    collection.drop()
    con.close()


if __name__ == '__main__':
    # test_get_databases()
    # test_show_collections('tina_db')
    # test_find_all_documents('tina_db', 'movies')
    # test_find_all_documents('tina_db', 'movies', {'id': 1})
    # test_find_all_documents('tina_db', 'movies', {'title': {'$regex': '^j', '$options': 'i'}})
    # test_find_all_documents('tina_db', 'movies', {'title': {'$regex': '.* W'}})

    # test_show_collections('tina_db')
    # test_drop_collection('tina_db', 'movies')
    # test_show_collections('tina_db')

    # test_insert_some_documents('tina_db', 'movies')
    # test_find_all_documents('tina_db', 'movies')

    # test_find_all_documents('tina_db', 'movies', {'Genre': {'$regex': '.*Drama'}}, {'Title': 1, 'Year': 1})
    test_find_all_documents('tina_db', 'movies', {'Genre': {'$regex': '.*Drama'}}, {'Title': 0, 'Year': 0})
