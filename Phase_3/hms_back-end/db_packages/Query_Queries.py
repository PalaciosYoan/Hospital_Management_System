import sqlite3
from sqlite3 import Error
import pandas as pd


class Query_Queries(object):
    #this will be use just to see avaliable companies and to see if we want to add more
    def get_maintence(self):
        try:
            query = """
                select * from Maintenance;
            """
            df = pd.read_sql_query(query, con=self.conn)
            return df
        except Error as e:
            self.conn.rollback()
            print(e)
    
    #####Hospital queries#####
    def get_hospitals(self):
        try:
            query = """
                select * from Hospital;
            """
            df = pd.read_sql_query(query, con=self.conn)
            return df
        except Error as e:
            self.conn.rollback()
            print(e)
    
    #complex 1
    def get_avaliable_maintence(self, h_name):
        '''This will retrieved any avaliable company that can be assigned to the given hospital'''
        try:
            #select h_id given hospital name
            #filtered maintenance junction table given h_id
            #filtered maintenance table given maint_id
            query = """
                select *
                from Maintenance,
                (select t1.maint_id 
                    from Hospital_Maintenance_Junction_Table t1,
                    (
                        select h_id from Hospital where name = '{}'
                    ) t5
                    where t1.h_id=t5.h_id
                ) t2
                where Maintenance.maint_id <> t2.maint_id
                ;
            """.format(h_name)
            df = pd.read_sql_query(query, con=self.conn)
            return df
        except Error as e:
            self.conn.rollback()
            print(e)
    #complex 8
    def get_maintence_given_hname(self, h_name):
        '''This will retrieved any avaliable company that can be assigned to the given hospital'''
        try:
            #select h_id given hospital name
            #filtered maintenance junction table given h_id
            #filtered maintenance table given maint_id
            query = """
                select *
                from Maintenance,
                (select t1.maint_id 
                    from Hospital_Maintenance_Junction_Table t1,
                    (
                        select h_id from Hospital where name = '{}'
                    ) t5
                    where t1.h_id=t5.h_id
                ) t2
                where Maintenance.maint_id == t2.maint_id
                ;
            """.format(h_name)
            df = pd.read_sql_query(query, con=self.conn)
            return df
        except Error as e:
            self.conn.rollback()
            print(e)
    
    def get_doctors_given_hospital(self, h_name):
        try:
            query = """
                select * 
                from Doctor,
                (
                    select h_id
                    from Hospital
                    where name = '{}'
                ) t1
                where Doctor.h_id=t1.h_id;
            """.format(h_name)
            df = pd.read_sql_query(query, con=self.conn)
            return df
        except Error as e:
            self.conn.rollback()
            print(e)
    
    #not using nurse h_id since we need a lot of complex queries
    #complex querie 2
    def get_nurses_given_hospital(self, h_name):
        try:
            query = """
                select Nurse.name, Nurse.started_working
                from Nurse, 
                    (select r_id 
                    from Room,
                        (
                            select h_id
                            from Hospital
                            where name = '{}'
                        ) h1
                    where Room.h_id = h1.h_id 
                    ) t2
                , Nurse_Room_Junction_Table t1
                where t2.r_id = t1.r_id 
                    and t1.n_id=Nurse.n_id;
                
            """.format(h_name)
            df = pd.read_sql_query(query, con=self.conn)
            return df
        except Error as e:
            self.conn.rollback()
            print(e)
    
    def get_patients_given_hospital(self, h_name):
        try:
            query = """
                select * 
                from Patient,
                        (
                            select h_id
                            from Hospital
                            where name = '{}'
                        ) h1
                where  Patient.h_id = h1.h_id;
            """.format(h_name)
            df = pd.read_sql_query(query, con=self.conn)
            return df
        except Error as e:
            self.conn.rollback()
            print(e)

    
    def get_medication_given_hospital(self, h_name):
        try:
            query = """
                select * 
                from Medication,
                        (
                            select h_id
                            from Hospital
                            where name = '{}'
                        ) h1
                
                where Medication.h_id=h1.h_id;
            """.format(h_name)
            df = pd.read_sql_query(query, con=self.conn)
            return df
        except Error as e:
            self.conn.rollback()
            print(e)

    def get_rooms_given_hospital(self, h_name):
        try:
            query = """
                select * 
                from Room,
                (
                            select h_id
                            from Hospital
                            where name = '{}'
                        ) h1
                where Room.h_id=h1.h_id;
            """.format(h_name)
            df = pd.read_sql_query(query, con=self.conn)
            return df
        except Error as e:
            self.conn.rollback()
            print(e)
            
    #complex query #3
    def get_maintenance_given_hospital(self, h_name):
        try:
            query = """
                select Maintenance.name, Maintenance.started_working, Maintenance.duty, Maintenance.phone_number
                from Maintenance,
                    (select *
                    from Hospital_Maintenance_Junction_Table j1,
                    (
                        select h_id
                        from Hospital
                        where name = '{}'
                    ) h1
                    where j1.h_id=h1.h_id) t1 
                    where
                        t1.maint_id = Maintenance.maint_id;
            """.format(h_name)
            df = pd.read_sql_query(query, con=self.conn)
            return df
        except Error as e:
            self.conn.rollback()
            print(e)
    
    
    #########Doctor Queries#########
    
    def get_patients_given_doctor(self, d_name):
        try:
            query = """
                select * 
                from Patient,
                (
                        select d_id
                        from Doctor
                        where name = '{}'
                    ) d1
                where Patient.d_id=d1.d_id;
            """.format(d_name)
            df = pd.read_sql_query(query, con=self.conn)
            return df
        except Error as e:
            self.conn.rollback()
            print(e)

    
    ##### Nurse Queries #########
    
    #complex query 4
    def get_patients_given_nurse(self, n_id):
        try:
            #given nurse id
            #query the junction table to filtered all rooms that current nurse is attending too
            # filtered Room table based on the rooms for current nurse
            # filtered patients corresponding to thsoe rooms
            query = """
                select Patient.name, Patient.dob, Patient.admit_date, Patient.released_data, Patient.problem, Patient.address,
                        Patient.phone_number
                from Room, Patient,
                (
                    select *
                    from 
                        Nurse_Room_Junction_Table
                    where n_id = '{}'
                ) t1
                where Room.r_id = t1.r_id
                    and Patient.p_id = Room.p_id;
            """.format(n_id)
            df = pd.read_sql_query(query, con=self.conn)
            return df
        except Error as e:
            self.conn.rollback()
            print(e)
    
    #complex query 5
    def get_rooms_given_nurse(self, n_name):
        try:
            query = """
                select Room.room_number, Room.person_allowed, Room.cost, Room.type
                from Room,
                (
                    select *
                    from 
                        Nurse_Room_Junction_Table t1,
                        (
                            n_id as nurse_id
                            from Nurse
                            where name = '{}'
                        )
                    where n_id = nurse_id
                ) t1
                where t1.r_id = Room.r_id;
            """.format(n_name)
            df = pd.read_sql_query(query, con=self.conn)
            return df
        except Error as e:
            self.conn.rollback()
            print(e)
    
    
    #patients
    #complex 6
    def get_prescribedMed_given_patient(self, patient_name):
        try:
            query = """
                select *
                from Medication,
                    (
                        select m_id, assigned_date
                        from Prescribed_Med pm,
                            (
                                select p_id as patient_id
                                from Patient
                                where name = '{}'
                            ) p1
                        where p_id = patient_id
                    ) t1
                where
                    t1.m_id = Medication.m_id;
            """.format(patient_name)
            df = pd.read_sql_query(query, con=self.conn)
            return df
        except Error as e:
            self.conn.rollback()
            print(e)