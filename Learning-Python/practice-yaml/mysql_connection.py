import sqlalchemy


class MysqlConnection:

    @classmethod
    def make_connection(cls, host, port, user, password, database):
        conn = sqlalchemy.create_engine(f"mysql+mysqlconnector://{user}:{password}@{host}:{port}/{database}")
        return conn
