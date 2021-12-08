
import sqlite3
from datetime import datetime
from sqlite3 import Error
import pandas as pd
class Update_Queries(object):
    ########Patient updates################
    #release date
    def update_patient(self,
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
                       r_id):
        try:
            q = """
                Update
                    Patient
                SET 
                    dob = "{}",
                    admit_date = "{}",
                    released_date = "{}",
                    problem = "{}",
                    address = "{}",
                    name = "{}",
                    phone_number = {},
                    h_id = "{}",
                    d_id = "{}",
                    r_id = "{}"
                WHERE
                    p_id = "{}"
            """.format(
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
                    p_id
                )
            self.conn.execute(q)
            self.conn.commit()
        except Error as e:
            self.conn.rollback()
            print(e)
    
    #doctor
    def update_doctor(self,
                    d_id,
                    name,
                    started_working,
                    phone_number,
                    h_id):
        
        try:
            q = """
                UPDATE Doctor
                SET
                    name = "{}",
                    started_working = "{}",
                    phone_number = {},
                    h_id = "{}"
                Where
                    d_id = "{}"
            """.format(
                    name,
                    started_working,
                    phone_number,
                    h_id,
                    d_id
                )
            self.conn.execute(q)
            self.conn.commit()
        except Error as e:
            self.conn.rollback()
            print(e)
    
    def update_hospital(self, h_id, address, name):
        try:
            q = """
                UPDATE Hospital
                SET
                    name = "{}",
                    address = "{}"
                where
                    h_id = "{}"
            """.format(name, address, h_id)
            self.conn.execute(q)
            self.conn.commit()
        except Error as e:
            self.conn.rollback()
            print(e)
    
    def update_maintenance(self, 
                            maint_id, 
                            name,
                            started_working,
                            duty,
                            phone_number):
        try:
            q = """
                UPDATE Hospital
                SET
                    name = "{}",
                    started_working = "{}",
                    duty = "{}",
                    phone_number = {}
                where
                    maint_id = "{}"
            """.format(
                        name,
                        started_working,
                        duty,
                        phone_number,
                        maint_id)
            self.conn.execute(q)
            self.conn.commit()
        except Error as e:
            self.conn.rollback()
            print(e)
    
    def update_medication(self,
                       m_id, 
                       cost, 
                       name, 
                       type, 
                       side_effect, 
                       h_id, 
                       treatment_for):
        try:
            q = """
                Update
                    Medication
                SET 
                    cost = {}, 
                    name = "{}", 
                    type = "{}", 
                    side_effect = "{}", 
                    h_id = "{}", 
                    treatment_for = "{}"
                WHERE
                    m_id = "{}"
            """.format(
                    cost, 
                    name, 
                    type, 
                    side_effect, 
                    h_id, 
                    treatment_for,
                    m_id
                )
            self.conn.execute(q)
            self.conn.commit()
        except Error as e:
            self.conn.rollback()
            print(e)