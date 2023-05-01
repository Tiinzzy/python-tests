from mysql_connection import MysqlConnection
import pandas as pd


def insert_in_mongodb(data):
    print(data)


def get_mysql_data(mysql_table):
    mysql = MysqlConnection()
    con, cur = mysql.open_database()
    query = "Select * from tests.TBALE_NAME;".replace('TBALE_NAME', mysql_table)

    df_result = pd.read_sql(query, con)
    # average_above_eight = df_result.loc[df_result['vote_average'] >= 8]
    result = df_result.to_dict(orient='records')

    mysql.close_database()

    return result
