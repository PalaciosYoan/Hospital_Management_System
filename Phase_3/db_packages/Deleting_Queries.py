from sqlite3 import Error


class Deleting_Queries(object):

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
    
    def delete_specific_maintenance(self, maint_id):
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