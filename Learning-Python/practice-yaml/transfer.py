from mysql_connection import MysqlConnection
from mongodb_connection import MongodbConnection
import pandas as pd
import csv


def insert_in_mysql(data):
    print(data)


def get_csv_data(csv_location):
    content = []
    with open(csv_location) as csvfile:
        csv_reader = csv.reader(csvfile)
        headers = next(csv_reader)

        for row in csv_reader:
            row_data = {key: value for key, value in zip(headers, row)}
            content.append(row_data)

    return content


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
