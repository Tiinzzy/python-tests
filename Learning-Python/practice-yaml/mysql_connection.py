import mysql.connector as connection


class MysqlConnection:

    @classmethod
    def open_database(cls, host, port, user, password, database):
        MysqlConnection.con = connection.connect(
            user=user, password=password, host=host, database=database, port=port, use_pure=True)
        return MysqlConnection.con, MysqlConnection.con.cursor()

    @classmethod
    def close_database(cls):
        MysqlConnection.con.cursor().close()
        MysqlConnection.con.close()
