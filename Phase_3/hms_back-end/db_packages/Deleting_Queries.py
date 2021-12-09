from sqlite3 import Error
import pandas as pd
class Deleting_Queries(object):
    def delete_specific_medication(self, m_name, h_name):
        try:
            #deletes medication from specific hospital
            #gets h id
            q = """
                select h_id
                from Hospital
                where name = "{}"
            """.format(h_name)
            self.cursor.execute(q)
            h_id = self.cursor.fetchall()[0][0]
            
            q = """
                select m_id 
                from Medication
                where name = "{}" and h_id = "{}"
                """.format(m_name, h_id)
            self.cursor.execute(q)
            m_id = self.cursor.fetchall()[0][0]
            
            query = """
                    DELETE 
                    FROM Medication,
                    WHERE 
                        m_id = "{}";
            """.format(m_id)
            self.conn.execute(query)
            
            query1 = """
                    DELETE 
                    FROM Prescribed_Med,
                    WHERE 
                        m_id = "{}";
            """.format(m_id)
            self.conn.execute(query1)
            
            self.conn.commit()
            
        except Error as e:
            self.conn.rollback()
            print(e)
    
    def delete_specific_prescribed_med(self,dob, p_name, med_name, h_name):
        try:
            #deletes prescribed med given teh patient id
            p_id = """
                select p_id, h_id
                from Patient
                Where
                    name = "{}" and dob = "{}"
            """.format(p_name, dob)
            self.cursor.execute()
            p_id = self.cursor.fetchall()[0][0]
            h_id = self.cursor.fetchall()[0][1]
            
            med_id = """
                select m_id
                from Medication
                where h_id = "{}" and name = "{}";
                """.format(h_id, med_name)
            self.cursor.execute()
            med_id  = self.cursor.fetchall()[0][0]
            query = """
                    DELETE 
                    FROM Prescribed_Med,
                    WHERE m_id = "{}" and p_id = "{}";
            """.format(med_id, p_id)
            self.conn.execute(query)
            self.conn.commit()
        
        except Error as e:
            self.conn.rollback()
            print(e)
    
    
    def delete_specific_maintenance_junc_hos(self, h_name, maint_name):
        try:
            #deletes specific maintennance given h_name and maint_name
            h_id = """
                select h_id
                from Hospital
                where name="{}"
            """.format(h_name)
            self.cursor.execute(h_id)
            h_id = self.cursor.fetchall()[0][0]
            
            maint_id = """
                select maint_id
                from Maintenance
                where maint_name ="{}"
            """.format(maint_name)
            self.cursor.execute(maint_id)
            maint_id = self.cursor.fetchall()[0][0]
            
            query = """
                    DELETE
                    FROM Hospital_Maintenance_Junction_Table
                    where
                        h_id = "{}" and maint_id = "{}"
                    ;
            """.format(h_id, maint_id)
            self.conn.execute(query)
            self.conn.commit()

        except Error as e:
            self.conn.rollback()
            print(e)
    
    def delete_specific_nurse_junc_room(self, n_id, r_id):
        try:
            query = """
                    DELETE
                    FROM Nurse_Room_Junction_Table
                    where
                        n_id = "{}" and r_id = "{}"
                    ;
            """.format(n_id, r_id)
            self.conn.execute(query)
            self.conn.commit()

        except Error as e:
            self.conn.rollback()
            print(e)

    def delete_specific_maintenance(self, maint_name):
        try:
            #deletes the relation between the hospital if any
            query = """
                select maint_id
                from Maintenance
                where name = "{}"
                """.format(maint_name)
            self.cursor.execute(query)
            maint_id = self.cursor.fetchall()[0][0]
            
            query  = """
                DELETE 
                FROM Maintenance
                WHERE maint_id = "{}";
                """.format(maint_id)
            self.conn.execute(query)
            
            query1  = """
                DELETE 
                FROM Hospital_Maintenance_Junction_Table
                WHERE maint_id = "{}";
                """.format(maint_id)
            self.conn.execute(query1)
            self.conn.commit()
            
        except Error as e:
            self.conn.rollback()
            print(e)
    
    def delete_doctor(self, d_id):
        try:
            q = """
                DELETE
                from Doctor
                where 
                    d_id = "{}"
            """.format(d_id)
            self.conn.execute(q)
            self.conn.commit()
        except Error as e:
            self.conn.rollback()
            print(e)
    
    def delete_nurse(self, n_id):
        try:
            q1 = """
                DELETE
                from Nurse
                where 
                    n_id = "{}"
            """.format(n_id)
            self.conn.execute(q1)
            
            self.conn.commit()
        except Error as e:
            self.conn.rollback()
            print(e)

    def delete_patient(self, p_name, dob):
        try:
            query = """
                select p_id
                from Patient
                where name = "{}" and dob="{}"
                """.format(p_name, dob)
            self.cursor.execute(query)
            p_id = self.cursor.fetchall()[0][0]
            
            q = """
                DELETE
                from Patient
                where 
                    p_id = "{}"
            """.format(p_id)
            self.conn.execute(q)
            
            q1 = """
                DELETE
                from Prescribed_Med
                where 
                    p_id = "{}"
            """.format(p_id)
            self.conn.execute(q1)
            
            self.conn.commit()
        except Error as e:
            self.conn.rollback()
            print(e)
    
    def delete_hospital(self, h_id):
        try:
            query = """
                DELETE
                from Hospital
                where
                    h_id = "{}"
            """.format(h_id)
            self.conn.execute(query)
            self.conn.commit()
            
            query = """
                DELETE
                from Room
                where
                    h_id = "{}"
            """.format(h_id)
            self.conn.execute(query)
            self.conn.commit()
            
            query = """
                DELETE
                from Hospital_Maintenance_Junction_Table
                where
                    h_id = "{}"
            """.format(h_id)
            self.conn.execute(query)
            self.conn.commit()
            
            n_id = """
                select n_id
                from Nurse
                where h_id ="{}"
            """.format(h_id)
            df = pd.read_sql_query(n_id, con=self.conn)
            for index, row in df.iterrows():
                query = """
                    DELETE
                    from Nurse_Room_Junction_Table
                    where
                        n_id = "{}"
                """.format(row['n_id'])
                self.conn.execute(query)
                self.conn.commit()
            
            query = """
                DELETE
                from Nurse
                where
                    h_id = "{}"
            """.format(h_id)
            self.conn.execute(query)
            self.conn.commit()
            
            query = """
                DELETE
                from Doctor
                where
                    h_id = "{}"
            """.format(h_id)
            self.conn.execute(query)
            self.conn.commit()

            p_id = """
                select p_id
                from Patient
                where h_id ="{}"
            """.format(h_id)
            df = pd.read_sql_query(p_id, con=self.conn)
            for index, row in df.iterrows():
                query = """
                    DELETE
                    from Prescribed_Med
                    where
                        p_id = "{}"
                """.format(row['p_id'])
                self.conn.execute(query)
                self.conn.commit()
                
            query = """
                DELETE
                from Patient
                where
                    h_id = "{}"
            """.format(h_id)
            self.conn.execute(query)
            self.conn.commit()
            
            query = """
                DELETE
                from Medication
                where
                    h_id = "{}"
            """.format(h_id)
            self.conn.execute(query)
            self.conn.commit()
            
        except Error as e:
            self.conn.rollback()
            print(e)