from datetime import datetime
import uuid
from sqlite3 import Error
from numpy import ma
import pandas as pd
class Inserting_Queries(object):
    def insert_specific_medication(self, m_name, h_name, cost, type, side_effect, treament_for):
        try:
            #gets h_id first given h_name
            q1 = """
                select h_name
                from Hospital
                where name = '{}'
                limit 1;
            """.format(h_name)
            self.cursor.execute(q1)
            
            h_id = self.cursor.fetchall()[0][0]
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
    
    def insert_specific_prescribed_med(self, assigned_date, p_name, m_name, h_name):
        try:
            #get p_id given p_name
            q1 = """
                select p_id
                from Patient
                where name = '{}'
                limit 1;
            """.format(p_name)
            self.cursor.execute(q1)
            p_id = self.cursor.fetchall()[0][0]

            #get h_id given h_name
            q1 = """
                select h_id
                from Hospital
                where name = '{}'
                limit 1;
            """.format(h_name)
            self.cursor.execute(q1)
            h_id = self.cursor.fetchall()[0][0]
            
            #get m_id given m_name and h_id
            q1 = """
                select m_id
                from Medication
                where name = '{}' and h_id='{}'
                limit 1;
            """.format(m_name, h_id)
            self.cursor.execute(q1)
            m_id = self.cursor.fetchall()[0][0]
            
            #format properly the date
            assigned_date = datetime.strftime(assigned_date, f"%Y-%m-%d")
            
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
    
    #complex query number 7
    def insert_specific_maintenance(self, h_name, maint_name):
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