from datetime import datetime
import uuid
from sqlite3 import Error
from numpy import ma
import pandas as pd
class Inserting_Queries(object):
    def insert_specific_medication(self, m_name, h_id, cost, type, side_effect, treament_for):
        try:

            m_id = str(uuid.uuid4())
            query = """
                    insert into Medication(m_id, cost, name, type, side_effect, h_id, treament_for)
                    Values ('{}', {}, '{}', '{}', '{}', '{}', '{}');
            """.format(m_id, cost, m_name, type, side_effect, h_id, treament_for)
            self.conn.execute(query)
            self.conn.commit()
            
        except Error as e:
            self.conn.rollback()
            print(e)
    
    # def insert_specific_prescribed_med(self, assigned_date, p_name, dob, m_name, h_name):
    #     try:
    #         #get p_id given p_name
    #         q1 = """
    #             select p_id
    #             from Patient
    #             where name = "{}" and dob="{}"
    #             limit 1;
    #         """.format(p_name, dob)
    #         self.cursor.execute(q1)
    #         p_id = self.cursor.fetchall()[0][0]

    #         #get h_id given h_name
    #         q1 = """
    #             select h_id
    #             from Hospital
    #             where name = '{}'
    #             limit 1;
    #         """.format(h_name)
    #         self.cursor.execute(q1)
    #         h_id = self.cursor.fetchall()[0][0]
            
    #         #get m_id given m_name and h_id
    #         q1 = """
    #             select m_id
    #             from Medication
    #             where name = '{}' and h_id='{}'
    #             limit 1;
    #         """.format(m_name, h_id)
    #         self.cursor.execute(q1)
    #         m_id = self.cursor.fetchall()[0][0]
            
    #         #format properly the date
    #         assigned_date = datetime.strftime(assigned_date, f"%Y-%m-%d")
            
    #         pmed_id = str(uuid.uuid4())
    #         query = """
    #                 INSERT INTO Prescribed_Med(
    #                 pmed_id, assigned_date, p_id, m_id
    #                 ) 
    #                 VALUES 
    #                 (
    #                     "{}", 
    #                     "{}", 
    #                     "{}",
    #                     "{}"
    #                 );
    #         """.format(pmed_id, assigned_date, p_id, m_id)
    #         self.conn.execute(query)
    #         self.conn.commit()
        
    #     except Error as e:
    #         self.conn.rollback()
    #         print(e)
    
    def insert_specific_prescribed_med(self, p_id, m_id, assigned_date):
        try:
            #get p_id given p_name
            pmed_id = str(uuid.uuid4())
            query = """
                    INSERT INTO Prescribed_Med(
                    pmed_id, assigned_date, p_id, m_id
                    ) 
                    VALUES 
                    (
                        "{}",
                        "{}",
                        "{}",
                        "{}"
                    );
            
            """.format(pmed_id, assigned_date, p_id, m_id)
            self.conn.execute(query)
            self.conn.commit()
        
        except Error as e:
            self.conn.rollback()
            print(e)
    
    def insert_nurse_room_junction(self, n_id, r_id):
        try:
            #get p_id given p_name
            pmed_id = str(uuid.uuid4())
            query = """
                    INSERT INTO Nurse_Room_Junction_Table(
                    r_id, n_id
                    ) 
                    VALUES 
                    (
                        "{}",
                        "{}"
                    );
            
            """.format(r_id, n_id)
            self.conn.execute(query)
            self.conn.commit()
        
        except Error as e:
            self.conn.rollback()
            print(e)
    
    def insert_hospital(self, name, address):
        try:
            #get p_id given p_name
            h_id = str(uuid.uuid4())
            query = """
                    INSERT INTO Hospital(
                    h_id, address, name
                    ) 
                    VALUES 
                    (
                        "{}",
                        "{}",
                        "{}"
                    );
            """.format(h_id, address,name)
            self.conn.execute(query)
            self.conn.commit()
        
        except Error as e:
            self.conn.rollback()
            print(e)
    
    def insert_room(self, room_number, person_allowed, cost, type, h_id):
        try:
            #get p_id given p_name
            query = """
                select room_number
                from Room
                where h_id = "{}";
            """.format(h_id)
            df = pd.read_sql_query(query, con=self.conn)
            max_room = df['room_number'].max()
            r_id = str(uuid.uuid4())
            print(df)
            query = """
                    INSERT INTO Room(
                    r_id, room_number, person_allowed, cost, type, h_id, p_id
                    ) 
                    VALUES 
                    (
                        "{}",
                        {},
                        {},
                        {},
                        "{}",
                        "{}",
                        "{}"
                    );
            """.format(r_id, max_room+1, person_allowed, cost, type, h_id, 'nan')
            self.conn.execute(query)
            self.conn.commit()
        
        except Error as e:
            self.conn.rollback()
            print(e)
    
    #complex query number 7
    def insert_specific_maintenance_hos_junct(self, h_name, maint_name):
        try:
            #get h_id given h_name
            q1 = """
                select h_id
                from Hospital
                where name = '{}'
                limit 1;
            """.format(h_name)
            self.cursor.execute(q1)
            h_id = self.cursor.fetchall()[0][0]
            
            #get maint_id given maint_name
            q1 = """
                select maint_id
                from Maintenance
                where name = '{}'
                limit 1;
            """.format(maint_name)
            self.cursor.execute(q1)
            maint_id = self.cursor.fetchall()[0][0]
            query = """
                    INSERT INTO Hospital_Maintenance_Junction_Table(
                    h_id, maint_id
                    ) 
                    VALUES 
                    (
                        "{}", 
                        "{}"
                    );
            """.format(h_id, maint_id)
            self.conn.execute(query)
            self.conn.commit()
        
        except Error as e:
            self.conn.rollback()
            print(e)
    
    def insert_doctor(self, name, started_working, phone_number, h_name):
        try:
            h_id = """
                select h_id
                from Hospital
                where name = "{}"
                """.format(h_name)
            self.cursor.execute(h_id)
            h_id = self.cursor.fetchall()[0][0]
            d_id = str(uuid.uuid4())
            
            query = f"""
                INSERT INTO Doctor
                VALUES("{d_id}", "{name}","{started_working}",{int(phone_number)}, "{h_id}")
            """#.format(d_id, name, datetime(started_working), int(phone_number), h_id)
            self.conn.execute(query)
            self.conn.commit()
        except Error as e:
            self.conn.rollback()
            print(e)
    
    def insert_nurse(self, name, started_working, h_name):
        try:
            h_id = """
                select h_id
                from Hospital
                where name = "{}"
                """.format(h_name)
            self.cursor.execute(h_id)
            h_id = self.cursor.fetchall()[0][0]
            n_id = str(uuid.uuid4())
            
            query = f"""
                INSERT INTO Nurse
                VALUES("{n_id}", "{started_working}","{name}", "{h_id}")
            """#.format(n_id,started_working, name, h_id)
            print(query)
            self.conn.execute(query)
            self.conn.commit()
        except Error as e:
            self.conn.rollback()
            print(e)
    
    def insert_maint(self, name, started_working, phone_number, duty):
        try:
            maint_id = str(uuid.uuid4())
            
            query = """
                INSERT INTO Maintenance
                VALUES("{}", "{}","{}","{}", {})
            """.format(maint_id, name, started_working, duty, phone_number)
            self.conn.execute(query)
            self.conn.commit()
        except Error as e:
            self.conn.rollback()
            print(e)
    
    
    def insert_patient(self,
                       dob, 
                       admit_date, 
                       released_date, 
                       problem, 
                       address, 
                       name, 
                       phone_number, 
                       h_id, 
                       d_id, 
                       r_id,
                       m_id):
        try:
            
            p_id = str(uuid.uuid4())
            q = """
                INSERT INTO
                    Patient
                VALUES (
                    "{}",
                    "{}",
                    "{}",
                    "{}",
                    "{}",
                    "{}",
                    "{}",
                    {},
                    "{}",
                    "{}",
                    "{}"
                    )
            """.format(
                    p_id,
                    dob, 
                    admit_date, 
                    released_date, 
                    problem, 
                    address, 
                    name, 
                    phone_number, 
                    h_id, 
                    d_id, 
                    r_id,
                )
            self.conn.execute(q)
            self.conn.commit()
            self.insert_specific_prescribed_med(p_id,m_id, admit_date)
            
        except Error as e:
            self.conn.rollback()
            print(e)