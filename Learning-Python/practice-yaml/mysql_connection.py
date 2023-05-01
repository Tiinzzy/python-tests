import mysql.connector as connection


class MysqlConnection:

    @classmethod
    def open_database(cls):
        MysqlConnection.con = connection.connect(
            user='dbadmin', password='washywashy', host='127.0.0.1', database='tests', use_pure=True)
        return MysqlConnection.con, MysqlConnection.con.cursor()

    @classmethod
    def close_database(cls):
        MysqlConnection.con.cursor().close()
        MysqlConnection.con.close()
