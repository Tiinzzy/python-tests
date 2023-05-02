from mysql_connection import MysqlConnection
from mongodb_connection import MongodbConnection
import pandas as pd
import csv


def create_table(columns, database, table):
    create_table_sql = ''
    for i in range(len(columns)):
        create_table_sql += "`" + columns[i].lower() + "` text(1000)" + (", " if i < len(columns) - 1 else "")

    result = f"""CREATE TABLE {database}.{table} (
                 {create_table_sql}
                                    );"""""
    return result


def insert_in_mysql_from_mongodb(data, host, port, user, password, database, table):
    columns = list()
    for i in range(len(data)):
        c = list(data[i].keys())
        if c not in columns:
            columns.append(c)

    biggest = max(columns)
    full_data = dict()
    for i in range(len(data)):
        columns = data[i].keys()
        columns = list(columns)

        print(data[i])
        if biggest[i] in columns[i]:
            full_data[biggest[i]] = columns[data[i]].values()
        else:
            full_data[biggest[i]] = None
    print(full_data)


def get_mongodb_documents(host, port, schema, collection):
    client = MongodbConnection(host, port)
    connection = client.connect()
    if connection:
        data = client.get_documents(schema, collection)
        client.disconnect()
        return data
    else:
        print('something went wrong')
        return False


def insert_in_mysql(data, database, table, host, port, user, password):
    columns = data[0].keys()
    columns = list(columns)

    mysql = MysqlConnection().make_connection(host, port, user, password, database)
    conn = mysql.connect()

    drop_sql = f"DROP TABLE IF EXISTS {database}.{table};"
    conn.execute(drop_sql)

    insert_sql = create_table(columns, database, table)

    conn.execute(insert_sql)

    for i in range(len(data)):
        rows = data[i].values()
        rows = '","'.join(rows)
        insert_into_table = f"""INSERT INTO {database}.{table}
                    VALUES ("{rows}");
                        """
        conn.execute(insert_into_table)

    conn.close()
    mysql.dispose()


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
