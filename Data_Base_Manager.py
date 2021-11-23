import sqlite3
from sqlite3 import Error
import uuid
import pandas as pd


class Data_Base_Manager:
    def __init__(self, db_path = r'hsm.db') -> None:
        self.conn = self.__set_connection(db_path)
        self.cursor = self.conn.cursor()
        self.__create_tables()
    
    def __set_connection(self, db_path):
        print("++++++++++++++++++++++++++++++++++")
        print("Open database: ", db_path)

        conn = None
        try:
            conn = sqlite3.connect(db_path)
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
    
    def delete_specific_hospital(self, id):
        try:
            #Deletes hospital from hospital table
            query = """
                    DELETE FROM Hospital WHERE h_id=?;
            """
            self.conn.execute(query, (id))
            self.conn.commit()
            try:
                #deletes instance of hospital and maintenance 
                query = """
                        DELETE FROM Hospital_Maintenance_Junction_Table WHERE h_id=?;
                    """
                self.conn.execute(query, (id))
                self.conn.commit()
                
                #gets room id for the hospital that was deleted
                query = """
                    SELECT r_id FROM Room WHERE h_id=?;
                """
                self.cursor.execute(query, (id))
                r_id = self.cursor.fetchall()
                r_id = r_id[0][0]
                try:
                    #Deletes all rooms corresponding to the hospital that was deleted
                    query = """
                        DELETE FROM Room WHERE h_id=?;
                    """
                    self.conn.execute(query, (id))
                    self.conn.commit()
                    
                    #Deletes the room and nurse connection too since room was deleted
                    query = """
                        DELETE FROM Nurse_Room_Junction_Table WHERE r_id=?;
                    """
                    self.conn.execute(query, (r_id))
                    self.conn.commit()
                except:
                    print("")

            except:
                print("")
        except Error as e:
            self.conn.rollback()
            print(e)
            
    def delete_specific_doctor(self, id):
        try:
            #deletes specific doctor
            query = """
                    DELETE FROM Doctor WHERE d_id=?;
            """
            self.conn.execute(query, (id))
            self.conn.commit()
        except Error as e:
            self.conn.rollback()
            print(e)
    
    def delete_specific_nurse(self, id):
        try:
            #deletes specific nurse
            query = """
                    DELETE FROM Nurse WHERE n_id=?;
            """
            self.conn.execute(query, (id))
            self.conn.commit()
            try:
                #deletes connection between nurse and room
                query = """
                    DELETE FROM Nurse_Room_Junction_Table WHERE n_id=?;
                """
                self.conn.execute(query, (id))
                self.conn.commit()
            except:
                print("")
        except Error as e:
            self.conn.rollback()
            print(e)
    
    def delete_specific_medication(self, m_id, h_id):
        try:
            #deletes medication from specific hospital
            query = """
                    DELETE FROM Medication WHERE m_id=? and h_id=?;
            """
            self.conn.execute(query, (m_id,h_id))
            self.conn.commit()
            try:
                #deletes medication from prescribed med since patient will no longer have that medication
                query = """
                    DELETE FROM Prescribed_Med WHERE m_id=?;
                """
                self.conn.execute(query, (m_id))
                self.conn.commit()
            except:
                print("")
        except Error as e:
            self.conn.rollback()
            print(e)
    
    def delete_specific_prescribed_med(self, p_id):
        try:
            #deletes prescribed med given teh patient id
            query = """
                    DELETE FROM Prescribed_Med WHERE p_id=?;
            """
            self.conn.execute(query, (p_id))
            self.conn.commit()
        
        except Error as e:
            self.conn.rollback()
            print(e)
    
    def delete_specific_prescribed_med(self, maint_id):
        try:
            #deletes prescribed med given teh patient id
            query = """
                    DELETE FROM Maintenance WHERE maint_id=?;
            """
            self.conn.execute(query, (maint_id))
            self.conn.commit()
            try:
                #deletes connection between nurse and room
                query = """
                    DELETE FROM Hospital_Maintenance_Junction_Table WHERE maint_id=?;
                """
                self.conn.execute(query, (maint_id))
                self.conn.commit()
            except:
                print("")
        except Error as e:
            self.conn.rollback()
            print(e)
    
    def delete_doctor_given_hospital_doc(self, h_name, d_name):
        try:
            query = """
                DELETE FROM 
                Doctor 
                WHERE 
                Doctor.h_id = (
                    SELECT 
                    Doctor.h_id 
                    FROM 
                    Hospital, 
                    Doctor 
                    where 
                    Hospital.name = '?' 
                    and Hospital.h_id = Doctor.h_id 
                    and Doctor.name = '?'
                );
            """
            self.conn.execute(query, (h_name, d_name))
            self.conn.commit()
        except Error as e:
            self.conn.rollback()
            print(e)
    
    def delete_realeased_patient(self):
        try:
            query = """
                DELETE FROM 
                Patient 
                WHERE 
                p_id NOT IN (
                    SELECT 
                    p_id 
                    FROM 
                    Patient 
                    WHERE 
                    released_date = ''
                );
            """
            self.conn.execute(query)
            self.conn.commit()
        except Error as e:
            self.conn.rollback()
            print(e)
    
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
x = Data_Base_Manager()