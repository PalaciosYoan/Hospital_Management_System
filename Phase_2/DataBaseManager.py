import sqlite3



class DataBaseManager:
    def __init__(self) -> None:
        self.set_connection()
        
    def set_connection(self):
        self.conn  = sqlite3.connect('h_db.sqlite')
        self.c = self.conn.cursor()
    
    def create_tables(self):
        with open("hms_create_tables.sql") as sql_file:
            create_table_queries = sql_file.read()
        self.c.executescript(create_table_queries)
    
    def drop_tables(self):
        with open("hms_drop_tables.sql") as sql_file:
            drop_table_queries = sql_file.read()
        self.c.executescript(drop_table_queries)
    
    def update_tables(self):
        with open("hms_insert_tables.sql") as sql_file:
            insert_data_queries = sql_file.read()
        self.c.executescript(insert_data_queries)