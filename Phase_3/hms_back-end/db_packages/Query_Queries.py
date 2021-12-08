import sqlite3
from datetime import datetime
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
    
    def get_maintenance(self, name):
        try:
            query = """
                select * from Maintenance where name = "{}";
            """.format(name)
            df = pd.read_sql_query(query, con=self.conn)
            return df
        except Error as e:
            self.conn.rollback()
            print(e)
    
    def get_hospital_given_maintence(self, maint_name):
        #Yoan
        try:
            #select h_id given hospital name
            #filtered maintenance junction table given h_id
            #filtered maintenance table given maint_id
            query = """
                select *
                from Hospital,
                (select t1.h_id 
                    from Hospital_Maintenance_Junction_Table t1,
                    (
                        select maint_id
                        from Maintenance
                        where name = "{}"
                    ) t5
                    where t1.maint_id=t5.maint_id
                ) t2
                where Hospital.h_id = t2.h_id
                ;
            """.format(maint_name)
            df = pd.read_sql_query(query, con=self.conn)
            return df
        except Error as e:
            self.conn.rollback()
            print(e)
    #complex 1
    def get_avaliable_maintence(self, h_name):
        """This will retrieved any avaliable company that can be assigned to the given hospital"""
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
                        select h_id from Hospital where name = "{}"
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
        """This will retrieved any avaliable company that can be assigned to the given hospital"""
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
                        select h_id from Hospital where name = "{}"
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
                    where name = "{}"
                ) t1
                where Doctor.h_id=t1.h_id;
            """.format(h_name)
            df = pd.read_sql_query(query, con=self.conn)
            return df
        except Error as e:
            self.conn.rollback()
            print(e)
    
    def get_doctors_given_hospital_doc_name(self, h_name, d_name):
        try:
            query = """
                select * 
                from Doctor,
                (
                    select h_id
                    from Hospital
                    where name = "{}"
                ) t1
                where Doctor.h_id=t1.h_id and
                    Doctor.name = "{}";
            """.format(h_name, d_name)
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
                            where name = "{}"
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
    
    def get_nurse_given_hospital_nurse_name(self, h_name, n_nurse):
        try:
            query = """
                select *
                from Nurse, Hospital
                where
                    Nurse.h_id = Hospital.h_id and
                    Hospital.name = "{}" and
                    Nurse.name = "{}";
            """.format(h_name, n_nurse)
            df = pd.read_sql_query(query, con=self.conn)
            return df
        except Error as e:
            self.conn.rollback()
            print(e)
    
    #complex Y
    def get_nurses_given_rooms(self, r_number, h_name):
        try:
            query = """
                select Nurse.name, Nurse.started_working
                from Nurse, 
                    (select n_id 
                    from Nurse_Room_Junction_Table,
                        (
                            select r_id
                            from Room,
                            (
                                select h_id
                                from Hospital
                                where
                                    name = "{}"
                            )h1
                            where room_number = {} and h1.h_id = Room.h_id
                        ) h1
                    where Nurse_Room_Junction_Table.r_id = h1.r_id 
                    ) t2
                where Nurse.n_id = t2.n_id;
                
            """.format(h_name,r_number)
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
                            where name = "{}"
                        ) h1
                where  Patient.h_id = h1.h_id;
            """.format(h_name)
            df = pd.read_sql_query(query, con=self.conn)
            return df
        except Error as e:
            self.conn.rollback()
            print(e)

    def get_patients_given_room(self, r_number, h_name):
        try:
            query = """
                select *
                from Patient, 
                    (select p_id 
                    from Room,
                        (
                            select h_id
                            from Hospital
                            where name = "{}"
                        ) h1
                    where Room.h_id = h1.h_id and room.room_number = {}
                    ) t2
                where Patient.p_id = t2.p_id;
                
            """.format(h_name, r_number)
            df = pd.read_sql_query(query, con=self.conn)
            return df
        except Error as e:
            self.conn.rollback()
            print(e)


    def get_rooms_not_filled(self, h_name):
        try:
            q = """
                select *
                from Room, Hospital
                where
                    Room.p_id = 'nan'
                    and Room.h_id = Hospital.h_id and
                    Hospital.name = "{}";
            """.format(h_name)
            df = pd.read_sql_query(q, con=self.conn)
            df = df.to_dict('records')
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
                            where name = "{}"
                        ) h1
                
                where Medication.h_id=h1.h_id;
            """.format(h_name)
            df = pd.read_sql_query(query, con=self.conn)
            return df
        except Error as e:
            self.conn.rollback()
            print(e)
    
    def get_medication_given_hospital_med_name(self,h_name, m_name):
        try:
            q = """
                select *
                from Medication, 
                    (
                        select h_id from Hospital where name = "{}"
                    )h1
                where
                    Medication.h_id = h1.h_id AND
                    Medication.name = "{}";
            """.format(h_name, m_name)
            df = pd.read_sql_query(q, con=self.conn)
            return df
        except Error as e:
            self.conn.rollback()
            print(e)

    #complex
    def get_medication_given_patient(self, p_name, dob):
        try:
            query = """
                select name, cost, type, side_effect, treament_for,  assigned_date
                from Medication,
                        ( select assigned_date, m_id as med_id
                            from Prescribed_Med,
                            (
                                select p_id
                                from Patient
                                where name = "{}" and dob = "{}"
                                ) p1
                            where p1.p_id = Prescribed_Med.p_id
                        ) h1
                where Medication.m_id=h1.med_id;
            """.format(p_name, dob)
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
                            where name = "{}"
                        ) h1
                where Room.h_id=h1.h_id;
            """.format(h_name)
            df = pd.read_sql_query(query, con=self.conn)
            return df
        except Error as e:
            self.conn.rollback()
            print(e)
    
    
    def get_rooms_given_room(self, r_number, h_name):
        try:
            query = """
                select * 
                from Room,
                (
                            select h_id
                            from Hospital
                            where name = "{}"
                        ) h1
                where Room.h_id=h1.h_id and Room.room_number = {};
            """.format(h_name, r_number)
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
                        where name = "{}"
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
                        where name = "{}"
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
                    where n_id = "{}"
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
                            select n_id as nurse_id
                            from Nurse
                            where name = "{}"
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
    
    def get_patients_given_patient(self,name, dob):
        try:
            query = """
                select *
                from Patient
                where
                    name = "{}" and
                    dob = "{}"
            """.format(name, dob)
            df = pd.read_sql_query(query, con=self.conn)
            return df
        except Error as e:
            self.conn.rollback()
            print(e)
    
    #complex number X
    def get_patients_given_med(self,m_name, h_name):
        try:
            query = """
                select 
                    p.dob, p.admit_date, p.problem, p.address, p.name, p.phone_number
                from Patient p,
                (
                    select p_id
                    from Prescribed_Med,
                    (
                        select m_id
                        from Medication,
                        (
                            select h_id
                            from Hospital
                            where name = "{}"
                        ) h1
                        where
                            Medication.name = "{}" and h1.h_id = Medication.h_id ) t1
                    where
                        t1.m_id = Prescribed_Med.m_id
                ) m1
                where
                    p.p_id = m1.p_id;
            """.format(h_name, m_name)
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
                                where name = "{}"
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