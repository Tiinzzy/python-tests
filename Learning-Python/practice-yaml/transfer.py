from mysql_connection import MysqlConnection
from pymongo import MongoClient
import pandas as pd


def insert_in_mongodb(documents, mongo_host, mongo_port, mongo_schema, mongo_collection):
    connection = MongoClient(mongo_host, mongo_port)
    database = connection[mongo_schema]
    collection = database.get_collection(mongo_collection)

    collection.insert_many(documents)
    connection.close()


def get_mysql_data(mysql_table):
    mysql = MysqlConnection()
    con, cur = mysql.open_database()
    query = "Select * from tests.TBALE_NAME;".replace('TBALE_NAME', mysql_table)

    df_result = pd.read_sql(query, con)
    # average_above_eight = df_result.loc[df_result['vote_average'] >= 8]
    result = df_result.to_dict(orient='records')

    mysql.close_database()

    return result
