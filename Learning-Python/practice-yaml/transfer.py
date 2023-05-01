from mysql_connection import MysqlConnection
from mongodb_connection import MongodbConnection
import pandas as pd


def insert_in_mongodb(documents, mongo_host, mongo_port, mongo_schema, mongo_collection):
    client = MongodbConnection(mongo_host, mongo_port)
    connection = client.connect()
    if connection:
        client.insert(mongo_schema, mongo_collection, documents)
        client.disconnect()
    else:
        print('something went wrong')


def get_mysql_data(mysql_table, host, port, user, password, database):
    mysql = MysqlConnection().make_connection(host, port, user, password, database)

    conn = mysql.connect()
    query = "Select * from tests.TABLE_NAME;".replace('TABLE_NAME', mysql_table)

    df_result = pd.read_sql(query, conn)
    result = df_result.to_dict(orient='records')

    conn.close()
    mysql.dispose()
    return result
