from datetime import date
import pandas as pd
import sqlite3
from sqlite3 import Error

def connect(path):
    conn = None
    try:
        conn = sqlite3.connect(path)
        # conn = conn.cursor()
    except Error as e:
        print(e)
        exit()
    return conn


doctor = pd.read_csv('./data/doctor.csv')
hospital =pd.read_csv('./data/hospital.csv')
hospital_maint_junction = pd.read_excel('./data/hospital_maintenance_junction_table.xlsx')
maintenance = pd.read_excel('./data/Maintenance.xlsx')
medication = pd.read_excel('./data/medication.xlsx')
patient = pd.read_excel('./data/Patient.xlsx')
prescribed_med = pd.read_excel('./data/prescribed_med.xlsx')
nurse_room_junction_table = pd.read_excel('./data/nurse_room_junction_table.xlsx')
nurse = pd.read_excel('./data/nurse.xlsx')
rooms = pd.read_excel('./data/rooms.xlsx') 


def doctor1(conn):
    doctor_columns = ['d_id','name','started_working','phone_number','h_id']
    for index, row in doctor.iterrows():
        name = row['name']
        d_id = row['d_id']
        start_date = row['started_working']
        phone_num = row['phone_number']
        h_id = row['h_id']
        query = """
            INSERT INTO Doctor (d_id,name,started_working,phone_number,h_id)
            VALUES ('{}','{}','{}',{},'{}');
            """.format(d_id, name, start_date, phone_num, h_id)
        conn.execute(query)#, (d_id, name, start_date, phone_num, h_id))

def hospital1(conn):
    hospital_columns = ['h_id',	'address',	'name']
    for index, row in hospital.iterrows():
        name = row['name']
        address = row['address']
        h_id = row['h_id']
        query = """
            INSERT INTO Hospital VALUES (?,?,?);
            """#.format(h_id, address, name)
        conn.execute(query, (h_id, address, name))
        
def hospitalandmaint(conn):
    hospital_maint_junction_columns = ['h_id',	'maint_id']
    for index, row in hospital_maint_junction.iterrows():
        maint_id = row['maint_id']
        h_id = row['h_id']
        query = """
            INSERT INTO Hospital_Maintenance_Junction_Table (h_id,maint_id) VALUES ('{}','{}');
            """.format(h_id, maint_id)
        conn.execute(query)#, (h_id, maint_id))
def maint(conn):
    maintenance_columns = ['maint_id',	'name',	'started_working',	'duty',	'phone_number']
    for index, row in maintenance.iterrows():
        maint_id = str(row['maint_id'])
        name = str(row['name'])
        start_date = row['started_working'].to_pydatetime()
        duty = str(row['duty'])
        phone_number = row['phone_number']
        query = """
            INSERT INTO Maintenance (maint_id,name,started_working,duty,phone_number)
            VALUES ('{}','{}','{}','{}',{});
            """.format(maint_id, name, start_date, duty, phone_number)
        conn.execute(query)#, (maint_id, name, start_date, duty, int(phone_number)))

def medication1(conn):
    medication_columns = ['m_id',	'cost',	'name',	'type',	'side_effect',	'h_id',	'treament_for']
    for index, row in medication.iterrows():
        m_id = row['m_id']
        cost = row['cost']
        name = row['name']
        type = row['type']
        side_effects = row['side_effects']
        h_id = row['h_id']
        treament_for = row['treament_for']
        query = """
            INSERT INTO Medication (m_id,cost,name,type,side_effect,h_id,treament_for)
            VALUES ('{}',{},'{}','{}','{}','{}','{}');
            """.format(m_id, cost, name, type, side_effects, h_id, treament_for)
        print(query)
        conn.execute(query)#,(m_id, cost, name, type, side_effects, h_id, treament_for))
    
def nurse1(conn):
    nurse_columns = ['n_id',	'started_working',	'name',	'h_id']
    for index, row in nurse.iterrows():
        name = row['name']
        n_id = row['n_id']
        start_date = row['started_working'].to_pydatetime()
        h_id = row['h_id']
        query = """
            INSERT INTO Nurse (n_id,started_working,name,h_id)
            VALUES ('{}','{}','{}','{}');
            """.format(n_id, start_date, name, h_id)
        conn.execute(query)#, (n_id, start_date, name, h_id))

def roomandnurseJunct(conn):
    nurse_room_junction_table_columns = ['r_id',	'n_id']
    for index, row in nurse_room_junction_table.iterrows():
        r_id = row['r_id']
        n_id = row['n_id']
        query = """
            INSERT INTO Nurse_Room_Junction_Table (r_id,n_id)
            VALUES ('{}','{}');
            """.format(r_id, n_id)
        conn.execute(query)#, (r_id, n_id))

def patient1(conn):
    patient_columns = ['p_id',	'dob',	'admit_date',	'released_date',	'problem',	'address',	'name'	'phone_number',	'h_id',	'd_id',	'r_id']
    for index, row in patient.iterrows():
        p_id = row['p_id']
        dob = row['dob'].to_pydatetime()
        admit_date = row['admit_date'].to_pydatetime()
        released_date = row['released_date'].to_pydatetime()
        released_date = date.today()
        problem = row['problem']
        address = row['address']
        name = row['name']
        r_id = row['r_id']
        phone_number = row['phone_number']
        h_id = row['h_id']
        d_id = row['d_id']
        query = """
            INSERT INTO Patient (p_id,dob,admit_date,released_date,problem,address,name,phone_number, h_id, d_id, r_id)
            VALUES ('{}','{}','{}','{}','{}','{}','{}',{},'{}','{}','{}');
            """.format(p_id,dob, admit_date, released_date, problem, address, name, phone_number,h_id, d_id, r_id)
        conn.execute(query)#, (p_id,dob, admit_date, released_date, problem, address, name, phone_number,h_id, d_id, r_id))
        
def prescribeMed(conn):
    prescribed_med_columns = ['pmed_id'	'assigned_date'	'p_id'	'm_id']
    for index, row in prescribed_med.iterrows():
        assined_date = row['assined_date'].to_pydatetime()
        pmed_id = row['pmed_id']
        p_id = row['p_id']
        m_id = row['m_id']
        query = """
            INSERT INTO Prescribed_Med (pmed_id,assigned_date,p_id,m_id)
            VALUES ('{}','{}','{}','{}');
            """.format(pmed_id, assined_date, p_id, m_id)
        conn.execute(query)#, (pmed_id, assined_date, p_id, m_id))

def room1(conn):
    rooms_columns = ['r_id',	'room_number',	'person_allowed',	'cost',	'type'	'h_id',	'p_id']
    for index, row in rooms.iterrows():
        room_number = row['room_number']
        cost = row['cost']
        type = row['type']
        person_allowed = row['person_allowed']
        h_id = row['h_id']
        r_id = row['r_id']
        p_id = row['p_id']
        query = """
            INSERT INTO Room (r_id,room_number,person_allowed,cost,type,h_id,p_id)
            VALUES ('{}',{},'{}',{},'{}','{}','{}');
            """.format(r_id, room_number, person_allowed, cost, type, h_id, p_id)
        conn.execute(query)#, (r_id, room_number, person_allowed, cost, type, h_id, p_id))
        

def main():
    conn = connect(r"hsm.db")
    with conn:
        doctor1(conn)
        hospital1(conn)
        hospitalandmaint(conn)
        maint(conn)
        medication1(conn)
        nurse1(conn)
        roomandnurseJunct(conn)
        patient1(conn)
        prescribeMed(conn)
        room1(conn)
main()
