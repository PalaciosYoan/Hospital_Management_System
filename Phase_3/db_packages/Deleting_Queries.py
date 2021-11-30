from sqlite3 import Error
class Deleting_Queries(object):
    def delete_specific_medication(self, m_name, h_name):
        try:
            #deletes medication from specific hospital
            query = """
                    DELETE 
                    FROM Medication,
                    (
                        select h_id
                        from Hospital
                        where name = '{}'
                    ) t1
                    WHERE 
                        t1.h_id = Medication.h_id and
                        Medication.name = '{}';
            """.format(h_name, m_name)
            self.conn.execute(query)
            self.conn.commit()
            
        except Error as e:
            self.conn.rollback()
            print(e)
    
    def delete_specific_prescribed_med(self, p_name):
        try:
            #deletes prescribed med given teh patient id
            query = """
                    DELETE 
                    FROM Prescribed_Med,
                    (
                        select p_id
                        from Patient
                        Where
                            name = '{}'
                    ) t1
                    WHERE t1.p_id = Prescribed_Med.p_id;
            """.format(p_name)
            self.conn.execute(query)
            self.conn.commit()
        
        except Error as e:
            self.conn.rollback()
            print(e)
    
    #complex query number 7
    def delete_specific_maintenance(self, h_name, maint_name):
        try:
            #deletes specific maintennance given h_name and maint_name
            query = """
                    DELETE
                    FROM Hospital_Maintenance_Junction_Table,
                    (
                        select h_id
                        from Hospital
                        where name='{}'
                    ) t1,
                    (
                        select maint_id
                        from Maintenance
                        where maint_name = '{}'
                    ) t2
                    where
                        t1.h_id = Hospital_Maintenance_Junction_Table.h_id and
                        t2.maint_id = Hospital_Maintenance_Junction_Table.maint_id
                    ;
            """.format(h_name, maint_name)
            self.conn.execute(query)
            self.conn.commit()

        except Error as e:
            self.conn.rollback()
            print(e)
