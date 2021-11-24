import uuid
from sqlite3 import Error
import pandas as pd
class Inserting_Queries(object):
    def insert_hospital(self, name, address):
        try:
            hd_id = str(uuid.uuid4())
            query = """
                INSERT INTO Hospital(h_id, address, name) 
                VALUES 
                (
                    "?", 
                    "?", 
                    "?"
                );
            """
            self.conn.execute(query, (hd_id, address, name))
            self.conn.commit()

            room_df = pd.read_excel('./data/rooms.xlsx')
            room_df = room_df[['room_number','cost', 'type', 'person_allowed']].head(20)
            hd_id_list = []
            room_id = []
            for i in range(20):
                room_id.append(str(uuid.uuid4()))
                hd_id_list.append(hd_id)
            inserting_data = []
            for index, row in room_df.iterrows():
                inserting_data.append((room_id[index],row['room_number'],row['person_allowed'],row['cost'],row['type'],hd_id_list[index], ''))
            query = """
                INSERT INTO Room(
                r_id, room_number, person_allowed, cost, type, h_id, p_id
                ) 
                VALUES 
                (
                    "?", 
                    "?", 
                    "?",
                    "?",
                    "?", 
                    "?",
                    "?"
                );
            """
            self.conn.executemany(query, inserting_data)
            
        except Error as e:
            self.conn.rollback()
            print(e)

    def insert_maintenance_host_junction(self, maint_name, hospital_name):
        try:
            
            h_id = self.cursor.execute("""
                                        SELECT h_id FROM Hospital where name='?'
                                        """,(hospital_name)).fetchall()[0][0]
            maint_id = self.cursor.execute("""
                                        SELECT maint_id FROM Maintenance where name='?'
                                        """,(maint_name)).fetchall()[0][0]
            exists = self.cursor.execute("""
                                        SELECT * FROM Hospital_Maintenance_Junction_Table where maint_id=? and h_id='?'
                                        """,(maint_id, h_id)).fetchall()[0][0]
            if exists == '':
                print(f"This relation already exist or maintenance {maint_name} /hospital {hospital_name} does not exist")
                return
            
            query = """
                INSERT INTO Hospital_Maintenance_Junction_Table(h_id, maint_id) 
                VALUES 
                (
                    "?", 
                    "?"
                );
            """
            self.conn.execute(query, (h_id, maint_id))
            self.conn.commit()

            
            
        except Error as e:
            self.conn.rollback()
            print(e)
            
    def insert_maintenance(self, maint_name, started_working_date, duty, phone_number):
        try:
            maint_id = self.cursor.execute("""
                                        SELECT maint_id FROM Maintenance where name='?'
                                        """,(maint_name)).fetchall()[0][0]
    
            if maint_id == '':
                print(f"This maintenance:{maint_name} already exists")
                return
            
            maint_id = str(uuid.uuid4())
            query = """
                INSERT INTO Maintenance(maint_id, name, started, duty, phone_number) 
                VALUES 
                (
                    "?", 
                    "?",
                    "?", 
                    "?",
                    "?"
                );
            """
            self.conn.execute(query, (maint_id, maint_name, started_working_date, duty, phone_number))
            self.conn.commit()
            
        except Error as e:
            self.conn.rollback()
            print(e)