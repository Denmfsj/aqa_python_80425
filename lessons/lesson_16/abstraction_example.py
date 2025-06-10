# DB

from abc import ABC, abstractmethod


class DB(ABC):

    @abstractmethod
    def create_connection(self):
        pass

    @abstractmethod
    def create_cursor(self):
        pass

    @abstractmethod
    def close_connections(self):
        pass


class Psql(DB):

    def create_connection(self):
        print('Psql creating connection')

    def create_cursor(self):
        print('Psql creating cursor')

    def close_connections(self):
        print('Psql closing connection')



class MSSQL(DB):

    def create_connection(self):
        print('mssql creating connection')

    def create_cursor(self):
        print('mssql creating cursor')



class DbRequestExecutor:

    def __init__(self, db_name):

        if db_name == 'psql':
            # створення інстансу
            self.db = Psql()  # bridge - паттерн

        elif db_name == 'mssql':
            self.db = MSSQL()

    def get_user_data_by_user_id(self, user_id):

        self.db.create_connection()
        self.db.create_cursor()
        print('sending query...')
        self.db.close_connections()


# psql_db = DbRequestExecutor(db_name='psql')
# psql_db.get_user_data_by_user_id(17)


mssql_db = DbRequestExecutor(db_name='mssql')
mssql_db.get_user_data_by_user_id(17)

