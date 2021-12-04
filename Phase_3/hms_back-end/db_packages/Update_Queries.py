
import sqlite3
from datetime import datetime
from sqlite3 import Error
import pandas as pd
class Update_Queries(object):
    ########Patient updates################
    #release date
    def update_released_date(self, released_date, name, dob):
        try:
            q = """
                Update
                    Patient
                SET 
                    released_date = "{}"
                WHERE
                    dob = "{}" and
                    name = "{}"
            """.format(released_date, dob, name)
            self.conn.execute(q)
            self.conn.commit()
        except Error as e:
            self.conn.rollback()
            print(e)
    
    #doctor
    def update_doctor(self, d_name_new, name, dob):
        
        try:
            d_name_new = """
                select d_id
                FROM Doctor
                WHERE name = "{}"
                limit 1;
            """.format(d_name_new)
            
            self.cursor.execute(d_name_new)
            d_name_new = self.cursor.fetchall()[0][0] #[[d_id]]
            if d_name_new == '':
                print("No updates were made because doctor does not exist")
                return

            q = """
                Update
                    Patient
                SET 
                    d_id = "{}"
                WHERE
                    dob = "{}" and
                    name = "{}"
            """.format(d_name_new, dob, name)
            self.conn.execute(q)
            self.conn.commit()
        except Error as e:
            self.conn.rollback()
            print(e)
    