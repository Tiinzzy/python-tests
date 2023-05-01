from pymongo import MongoClient
import pandas as pd
import mysql.connector as sql


def insert_in_mongodb(documents, mongo_host, mongo_port, mongo_schema, mongo_collection):
    connection = MongoClient(mongo_host, mongo_port)
    database = connection[mongo_schema]
    collection = database.get_collection(mongo_collection)

    collection.insert_many(documents)
    connection.close()


def get_mysql_data(mysql_table, mysql_host, mysql_port, mysql_user, mysql_password, mysql_schema):
    db_connection = sql.connect(host=mysql_host, database=mysql_schema, user=mysql_user, password=mysql_password,
                                port=mysql_port)
    db_cursor = db_connection.cursor()
    query = "Select * from tests.TBALE_NAME;".replace('TBALE_NAME', mysql_table)
    db_cursor.execute(query)
    table_rows = db_cursor.fetchall()
    df = pd.DataFrame(table_rows)
    print(df)

    # return result
