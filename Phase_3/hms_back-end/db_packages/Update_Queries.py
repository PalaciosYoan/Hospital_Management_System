
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
                        problem,
                        address,
                        released_date,
                        name,
                        phone_number,
                        h_id,
                        d_id,
                        r_id,
                        m_id):
        try:
            q = """
                Update
                    Patient
                SET 
                    p_id = "{}",
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
                    p_id
                )
            self.conn.execute(q)
            self.conn.commit()
            self.update_prescribed_med(p_id, 
                                       m_id,
                                       admit_date)
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
    
    def update_nurse(self,
                    n_id,
                    name,
                    started_working,
                    h_id):
        
        try:
            q = """
                UPDATE Nurse
                SET
                    name = "{}",
                    started_working = "{}",
                    h_id = "{}"
                Where
                    n_id = "{}"
            """.format(
                    name,
                    started_working,
                    h_id,
                    n_id
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
                    treament_for = "{}"
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
    
    def update_room(self,
                       r_id, 
                       room_number, 
                       person_allowed, 
                       cost, 
                       type, 
                       h_id, 
                       p_id):
        try:
            q = """
                Update
                    Patient
                SET 
                    room_number = {},
                    person_allowed = {},
                    cost = {},
                    type = "{}" ,
                    h_id = "{}",
                    p_id = "{}"
                WHERE
                    r_id = "{}"
            """.format(
                    room_number, 
                    person_allowed, 
                    cost, 
                    type, 
                    h_id, 
                    p_id,
                    r_id
                )
            self.conn.execute(q)
            self.conn.commit()
        except Error as e:
            self.conn.rollback()
            print(e)
    
    def update_hos_maint_junc(self, 
                              new_h_id, 
                              new_maint_id, 
                              old_h_id, 
                              old_maint_id):
        try:
            q = """
            UPDATE Hospital_Maintenance_Junction_Table
            SET h_id = "{}", maint_id ="{}"
            WHERE
                h_id = "{}", maint_id ="{}"
            """.format(new_h_id, new_maint_id, old_h_id, old_maint_id)
            self.conn.execute(q)
            self.conn.commit()
        except Error as e:
            self.conn.rollback()
            print(e)
    
    def update_nurse_room_junc(self, 
                              new_n_id, 
                              new_r_id, 
                              old_n_id, 
                              old_r_id):
        try:
            q = """
            UPDATE Hospital_Maintenance_Junction_Table
            SET n_id = "{}", r_id ="{}"
            WHERE
                n_id = "{}", r_id ="{}"
            """.format(new_n_id, new_r_id, old_n_id, old_r_id)
            self.conn.execute(q)
            self.conn.commit()
        except Error as e:
            self.conn.rollback()
            print(e)
    
    def update_prescribed_med(self, 
                              p_id, 
                              m_id,
                              assigned_date):
        try:
            q = """
            UPDATE Prescribed_Med
            SET 
                m_id = "{}"
            WHERE
                p_id = "{}"
            """.format(m_id, p_id)
            self.conn.execute(q)
            self.conn.commit()
        except Error as e:
            self.conn.rollback()
            print(e)