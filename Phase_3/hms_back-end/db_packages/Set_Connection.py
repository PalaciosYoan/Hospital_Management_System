import sqlite3
from sqlite3 import Error


class Set_Connection(object):
    def __init__(self, db_path = r'hsm.db') -> None:
        self.conn = self.__set_connection(db_path)
        self.cursor = self.conn.cursor()
        
    def __set_connection(self, db_path):
        print("++++++++++++++++++++++++++++++++++")
        print("Open database: ", db_path)

        conn = None
        try:
            conn = sqlite3.connect(db_path, check_same_thread=False)
            print("success")
        except Error as e:
            print(e)

        print("++++++++++++++++++++++++++++++++++")

        return conn

    def close_Connection(self,db_path):
        print("++++++++++++++++++++++++++++++++++")
        print("Close database: ", db_path)

        try:
            self.conn.close()
            print("success")
        except Error as e:
            print(e)

        print("++++++++++++++++++++++++++++++++++")