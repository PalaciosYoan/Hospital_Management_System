from sqlite3 import Error
# from Set_Connection import Set_Connection
# from Deleting_Queries import Deleting_Queries
# from Inserting_Queries import Inserting_Queries
# from Query_Queries import Query_Queries
# from Update_Queries import Update_Queries
from db_packages.Set_Connection import Set_Connection
from db_packages.Deleting_Queries import Deleting_Queries
from db_packages.Inserting_Queries import Inserting_Queries
from db_packages.Query_Queries import Query_Queries
from db_packages.Update_Queries import Update_Queries

class Data_Base_Manager(Set_Connection, Deleting_Queries, Inserting_Queries, Query_Queries, Update_Queries):
    def __init__(self, db_path = r'hsm.db') -> None:
        super(Data_Base_Manager, self).__init__()
        self.__create_tables()
        
        
    def __create_tables(self):
        try:
            with open('./sql_queries/hms_create_tables.sql') as f:
                self.cursor.executescript(f.read())
            print("Successfully created tables if they don't exist")
        except Error as e:
            self.conn.rollback()
            print(e)

    def drop_all_tables(self):
        try:
            with open('./sql_queries/hms_drop_tables.sql') as f:
                self.cursor.executescript(f.read())
            print("Successfully drop all tables")
        except Error as e:
            self.conn.rollback()
            print(e)

