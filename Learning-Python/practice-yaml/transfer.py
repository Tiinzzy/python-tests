from mysql_connection import MysqlConnection
from mongodb_connection import MongodbConnection
import pandas as pd


def insert_in_mongodb(documents, mongo_host, mongo_port, mongo_schema, mongo_collection):
    client = MongodbConnection(mongo_host, mongo_port)
    connection = client.connect()
    if connection:
        client.insert(mongo_schema, mongo_collection, documents)
    else:
        print('something went wrong')


def get_mysql_data(mysql_table, mysql_host, mysql_port, mysql_user, mysql_password, mysql_schema):
    mysql = MysqlConnection()
    con, cur = mysql.open_database(mysql_host, mysql_port, mysql_user, mysql_password, mysql_schema)
    query = "Select * from tests.TBALE_NAME;".replace('TBALE_NAME', mysql_table)

    df_result = pd.read_sql(query, con)
    # average_above_eight = df_result.loc[df_result['vote_average'] >= 8]
    result = df_result.to_dict(orient='records')
    mysql.close_database()

    return result
