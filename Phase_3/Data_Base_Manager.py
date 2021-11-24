from sqlite3 import Error
from db_packages.Set_Connection import Set_Connection
from db_packages.Deleting_Queries import Deleting_Queries
from db_packages.Inserting_Queries import Inserting_Queries

class Data_Base_Manager(Set_Connection, Deleting_Queries, Inserting_Queries):
    def __init__(self, db_path = r'hsm.db') -> None:
        super(Data_Base_Manager, self).__init__()
        
        self.delete_specific_medication('two', 'three')
        self.insert_hospital('m','2')
        
    def __create_tables(self):
        try:
            with open('./Phase_2/hms_create_tables.sql') as f:
                self.cursor.executescript(f.read())
            print("Successfully created tables if they don't exist")
        except Error as e:
            self.conn.rollback()
            print(e)

    def drop_all_tables(self):
        try:
            with open('./Phase_2/hms_drop_tables.sql') as f:
                self.cursor.executescript(f.read())
            print("Successfully drop all tables")
        except Error as e:
            self.conn.rollback()
            print(e)

x = Data_Base_Manager()