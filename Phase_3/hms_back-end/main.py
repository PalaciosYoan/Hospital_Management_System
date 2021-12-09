from numpy import delete
from db_packages.Data_Base_Manager import Data_Base_Manager
from flask import Flask, render_template, jsonify, request, redirect, session, g
from flask_restful import Api, Resource
from flask.helpers import url_for
from distutils.log import error
from flask_cors import CORS
import json

app = Flask(__name__)
api = Api(app)
db_manager = Data_Base_Manager()
CORS(app)
class allMaintenceAPI(Resource):
    def get(self):
        df = db_manager.get_maintence()
        df = df.to_dict('records')
        return df
class hospitalAPI(Resource):
    def get(self):
        df = db_manager.get_hospitals()
        df = df.to_dict('records')
        return df

    def post(self):
        try:
            action = json.loads(request.data)['queryType']
            if action == 'maint_name':
                maint_name = json.loads(request.data)['maint_name']
                df = db_manager.get_hospital_given_maintence(maint_name=maint_name)
                df = df.to_dict('records')
                return df
        except:
            
            action = json.loads(request.data)['formInput']['queryType']
            if action == 'post':
                data = json.loads(request.data)['formInput']
                h_name = data['name']
                address = data['address']
                db_manager.insert_hospital(h_name, address)
            elif action == 'delete':
                h_id = json.loads(request.data)['formInput']['h_id']
                db_manager.delete_hospital(h_id=h_id)
            
        
    def put(self):
        data = json.loads(request.data)['formInput']
        h_id = data['h_id']
        address = data['address']
        name = data['name']
        db_manager.update_hospital(h_id, address, name)
class avaliableMaintenceAPI(Resource):
    def post(self):
        #must send a json format {'hospital_name':hospital_name}
        hospital_name = json.loads(request.data)['hospital_name']
        df = db_manager.get_avaliable_maintence(hospital_name)
        df = df.to_dict('records')
        return df
    
    def put(self):
        data = json.loads(request.data)['formInput']
        new_h_id = data['new_h_id']
        new_maint_id = data['new_maint_id']
        old_h_id = data['old_h_id'] 
        old_maint_id = data['old_maint_id']
        db_manager.update_hos_maint_junc( 
                            new_h_id, 
                            new_maint_id, 
                            old_h_id, 
                            old_maint_id)

class MaintenceAPI(Resource):
    def post(self):
        #must send a json format {'hospital_name':hospital_name}
        try:
            action = json.loads(request.data)['queryType']
            if action == 'get':
                h_id = json.loads(request.data)['h_id']
                df = db_manager.get_maintenance_given_hospital(h_id)
                df = df.to_dict('records')
                return df
            elif action == 'post-junction-table':
                data = json.loads(request.data)['formInput']
                h_id = data['h_id']
                maint_id = data['maint_id']
                db_manager.insert_specific_maintenance_hos_junct(h_id, maint_id)
                return 'status: 200'
            elif action =='insert-maintenance': # easily be able to add more queries to doctor
                data = json.loads(request.data)['formInput']
                name = data['maint_name']
                started_working = data['start_date']
                phone_number = data['phone_number']
                duty = data['duty']
                db_manager.insert_maint(name, started_working, phone_number, duty)
            elif action == 'maintenance':
                maint_id = json.loads(request.data)['maint_id']
                df =db_manager.get_maintenance(maint_id)
                df = df.to_dict('records')
                return df
        except:
            given = json.loads(request.data)['formInput']
            if given['queryType'] == "junctionTable":
                h_name = given['hospital_name']
                maint_name = given['maintenance_name']
                db_manager.delete_specific_maintenance_junc_hos(h_name, maint_name)
                return
            if given['queryType'] == "maintTable":
                maint_name = given['maintenance_name']
                db_manager.delete_specific_maintenance(maint_name=maint_name)
                return
    def put(self):
        data = json.loads(request.data)['formInput']
        maint_id = data['maint_id']
        name = data['name']
        started_working = data['started_working']
        duty = data['duty']
        phone_number = data['phone_number']
        db_manager.update_maintenance(
            maint_id, 
            name,
            started_working,
            duty,
            phone_number
        )

class doctorAPI(Resource):
    def post(self):
        try:
            action = json.loads(request.data)['queryType']
            if action == 'hospital':
                hospital_name = json.loads(request.data)['hospital_name']
                df = db_manager.get_doctors_given_hospital(hospital_name)
                df = df.to_dict('records')
                return df
            elif action =='hospital-doctor': # easily be able to add more queries to doctor
                data = json.loads(request.data)
                hos_name = data['hospital_name']
                doc_name = data['doctor_name']
                df = db_manager.get_doctors_given_hospital_doc_name(hos_name, doc_name)
                df = df.to_dict('records')
                return df
        except:
            action = json.loads(request.data)['formInput']['queryType']
            if action =='insert-doctor': # easily be able to add more queries to doctor
                data = json.loads(request.data)['formInput']
                name = data['name']
                started_working = data['started_working']
                phone_number = data['phone_number']
                h_name = data['hospital_name']
                db_manager.insert_doctor(name, started_working, phone_number, h_name)
            elif action == 'delete':
                data = json.loads(request.data)['formInput']
                doc_id = data['d_id']
                db_manager.delete_doctor(d_id=doc_id)
    
    def put(self):
        data = json.loads(request.data)['formInput']
        d_id = data['d_id']
        name = data['name']
        started_working = data['started_working']
        phone_number = data['phone_number']
        h_id = data['h_id']
        db_manager.update_doctor(
                    d_id,
                    name,
                    started_working,
                    phone_number,
                    h_id)

class nurseAPI(Resource):
    def post(self):
        try:
            action = json.loads(request.data)['queryType']
            if action == 'hospital':
                h_id = json.loads(request.data)['h_id']
                df = db_manager.get_nurses_given_hospital(h_id)
                df = df.to_dict('records')
                return df
            elif action == "room":
                r_number = json.loads(request.data)["room_number"]
                h_name = json.loads(request.data)["hospital_name"]
                df = db_manager.get_nurses_given_rooms(r_number=r_number, h_name=h_name)
                df = df.to_dict('records')
                return df

                db_manager.insert_nurse(name, started_working, phone_number, h_name)
            elif action == 'nurse-hospital':
                data = json.loads(request.data)
                hospital_name = data['hospital_name']
                nurse_name = data['nurse_name']
                df = db_manager.get_nurse_given_hospital_nurse_name(hospital_name, nurse_name)
                df = df.to_dict('records')
                return df 
        except:
            action = json.loads(request.data)['formInput']['queryType']
            if action =='insert-nurse': # easily be able to add more queries to doctor
                data = json.loads(request.data)['formInput']
                name = data['name']
                started_working = data['started_working']
                h_name = data['hospital_name']
                db_manager.insert_nurse(
                    name,
                    started_working,
                    h_name
                )
            elif action == 'delete':
                data = json.loads(request.data)['formInput']
                n_id = data['n_id']
                db_manager.delete_nurse(n_id=n_id)
    
    def put(self):
        data = json.loads(request.data)['formInput']
        n_id = data['n_id']
        name = data['name']
        started_working = data['started_working']
        h_id = data['h_id']
        db_manager.update_nurse(
                    n_id,
                    name,
                    started_working,
                    h_id)

class patientAPI(Resource):
    def post(self):
        try:
            action = json.loads(request.data)['queryType']
            if action == 'hospital':
                hospital_name = json.loads(request.data)['hospital_name']
                df = db_manager.get_patients_given_hospital(hospital_name)
                df = df.to_dict('records')
                return df
            elif action == 'doctor':
                doctor_name = json.loads(request.data)['doctor_name']
                df = db_manager.get_patients_given_doctor(doctor_name)
                df = df.to_dict('records')
                return df
            elif action == 'nurse':
                nurse_name = json.loads(request.data)['nurse_name']
                df = db_manager.get_patients_given_nurse(nurse_name)
                df = df.to_dict('records')
                return df
            elif action == 'patient':
                patient_name = json.loads(request.data)['patient_name']
                dob = json.loads(request.data)['dob']
                df = db_manager.get_patients_given_patient(patient_name, dob)
                df = df.to_dict('records')
                return df
            elif action == 'medication':
                data = json.loads(request.data)
                m_name = data['med_name']
                h_name = data['hospital_name']
                df = db_manager.get_patients_given_med(m_name, h_name)
                df = df.to_dict('records')
                return df
            elif action == 'room':
                data = json.loads(request.data)
                r_number = data['room_number']
                h_name = data['hospital_name']
                df = db_manager.get_patients_given_room(r_number, h_name)
                df = df.to_dict('records')
                return df
        except:
            action = json.loads(request.data)['formInput']['queryType']
            if action == 'post-patient':
                data = json.loads(request.data)['formInput']
                dob = data['dob']
                admit_date = data['admit_date'] 
                released_date = data['released_date'] 
                problem = data['problem'] 
                address = data['address'] 
                name = data['name'] 
                phone_number = data['phone_number'] 
                h_id = data['h_id'] 
                d_id = data['d_id'] 
                r_id = data['r_id'] 
                m_id = data['m_id']
                db_manager.insert_patient(
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
                                        m_id)
            elif action == 'delete':
                data = json.loads(request.data)['formInput']
                p_id = data['p_id']
                db_manager.delete_patient(p_id=p_id)
        
        
    def put(self):
        data = json.loads(request.data)['formInput']
        p_id = data['p_id']
        dob = data['dob']
        admit_date = data['admit_date']
        released_date = data['released_date']
        problem = data['problem']
        address = data['address']
        name = data['name']
        phone_number = data['phone_number']
        h_id = data['h_id']
        d_id = data['d_id']
        r_id = data['r_id']
        m_id = data['m_id']
        db_manager.update_patient(
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
                            m_id
                        )
        return "Success 200"


class medicationAPI(Resource):
    def post(self):
        try:
            action = json.loads(request.data)['queryType']
            if action == 'get':
                hospital_name = json.loads(request.data)['hospital_name']
                df = db_manager.get_medication_given_hospital(hospital_name)
                df = df.to_dict('records')
                return df
            elif action == 'patient':
                patient_name = json.loads(request.data)['patient_name']
                dob = json.loads(request.data)['dob']
                df = db_manager.get_medication_given_patient(patient_name, dob)
                df = df.to_dict('records')
                return df
            elif action == 'hospital-med':
                json_data = json.loads(request.data)
                m_id = json_data['m_id']
                
                df = db_manager.get_medication_given_hospital_med_name(m_id)
                df = df.to_dict('records')
                return df
        except:
            action = json.loads(request.data)['formInput']['queryType']
            if action =='post':
                json_data = json.loads(request.data)['formInput']
                m_name = json_data['name']
                h_id = json_data['h_id']
                cost = json_data['cost']
                type = json_data['type']
                side_effect = json_data['side_effect']
                treament_for = json_data['treatment_for']
                db_manager.insert_specific_medication(m_name, h_id, cost, type, side_effect, treament_for)
                return 'status: 200'
            elif action == 'delete':
                m_id = json.loads(request.data)['formInput']['m_id']
                db_manager.delete_specific_medication(m_id)
                return 'status: 200'
        

    def put(self):
        data = json.loads(request.data)['formInput']
        m_id = data['m_id']
        cost = data['cost']
        name = data['name'] 
        type = data['type']
        side_effect = data['side_effect'] 
        h_id = data['h_id'] 
        treatment_for = data['treatment_for']
        db_manager.update_medication(
            m_id, 
            cost, 
            name, 
            type, 
            side_effect, 
            h_id, 
            treatment_for
        )
class getRooms(Resource):
    
    def post(self):
        try:
            action = json.loads(request.data)['queryType']
            if action == 'hospital':
                hospital_name = json.loads(request.data)['hospital_name']
                df = db_manager.get_rooms_given_hospital(hospital_name)
                df = df.to_dict('records')
                return df
            elif action == 'nurse':
                nurse_name = json.loads(request.data)['nurse_name']
                df = db_manager.get_rooms_given_nurse(nurse_name)
                df = df.to_dict('records')
                return df
            elif action == 'room':
                r_number = json.loads(request.data)['room_number']
                hospital_name = json.loads(request.data)['hospital_name']
                df = db_manager.get_rooms_given_room(r_number, hospital_name)
                df = df.to_dict('records')
                return df
            elif action == 'room_not_filled':
                h_name = json.loads(request.data)['hospital_name']
                return db_manager.get_rooms_not_filled(h_name)
        except:
            action = json.loads(request.data)['formInput']['queryType']
            if action == 'delete':
                data = json.loads(request.data)['formInput']
                r_num = data['room_number']
                n_name = data['nurse_name']
                db_manager.delete_specific_nurse_junc_room(r_num=r_num, n_name=n_name)
            elif action == 'delete-room':
                data = json.loads(request.data)['formInput']
                r_id = data['r_id']
                db_manager.delete_room(r_id)
            elif action == 'insert':
                data = json.loads(request.data)['formInput']
                h_id = data['h_id']
                person_allowed = data['person_allowed']
                cost = data['cost']
                type = data['type']
                db_manager.insert_room(person_allowed, cost, type, h_id)
                
    def put(self):
        data = json.loads(request.data)['formInput']
        person_allowed = data['person_allowed']
        cost = data['cost']
        type = data['type']
        r_id = data['r_id']
        db_manager.update_room(r_id, person_allowed, cost, type)

class getMaintenanceListForAHospital(Resource):
    def post(self):
        hospital_name = json.loads(request.data)['hospital_name']
        df = db_manager.get_maintenance_given_hospital(hospital_name)
        df = df.to_dict('records')
        return df
    

class prescribedMedsAPI(Resource):
    def post(self):
        try:
            action = json.loads(request.data)['queryType']
            if action == 'get':
                patient_name = json.loads(request.data)['patient_name']
                dob = json.loads(request.data)['dob']
                df = db_manager.get_medication_given_patient(patient_name, dob)
                df = df.to_dict('records')
                return df
        except:
            action = json.loads(request.data)['formInput']['queryType']
            
            if action == 'post':
                data = json.loads(request.data)['formInput']
                assigned_date = data['assigned_date']
                p_name = data['patient_name']
                m_name = data['medication_name']
                h_name = data['hospital_name']
                dob = data['dob']
                db_manager.insert_specific_prescribed_med(assigned_date, p_name, dob, m_name, h_name)
                return 'status: 200'
            elif action=='delete':
                data = json.loads(request.data)['formInput']
                patient_name = data['patient_name']
                dob = data['dob']
                hospital_name = data['hospital_name']
                med_name = data['medication_name']
                db_manager.delete_specific_prescribed_med(dob=dob, p_name=patient_name, med_name=med_name, h_name = hospital_name)
                return 'status: 200'
    
    def put(self):
        data = json.loads(request.data)['formInput']
        p_id = data['p_id'] 
        m_id = data['m_id']
        pmed_id = data['pmed_id']
        assigned_date = data['assigned_date']
        db_manager.update_prescribed_med(p_id, m_id, pmed_id, assigned_date)
    
    
class nuresRoomJunc(Resource):
    def post(self):
        action = json.loads(request.data)['formInput']['queryType']
        if action=='insert':
            data = json.loads(request.data)['formInput']
            n_id = data['n_id']
            r_id = data['r_id']
            db_manager.insert_nurse_room_junction(n_id, r_id)
        elif action == 'delete':
            data = json.loads(request.data)['formInput']
            n_id = data['n_id']
            r_id = data['r_id']

            db_manager.delete_specific_nurse_junc_room(n_id, r_id)

    
    def put(self):
        data = json.loads(request.data)['formInput']
        new_n_id = data['new_n_id']
        new_r_id = data['new_r_id']
        old_n_id = data['old_n_id'] 
        old_r_id = data['old_r_id']
        db_manager.update_nurse_room_junc( 
                            new_n_id, 
                            new_r_id, 
                            old_n_id, 
                            old_r_id)
    
api.add_resource(hospitalAPI, '/gethospital')
api.add_resource(allMaintenceAPI, '/getallMaintence')
api.add_resource(avaliableMaintenceAPI, '/getavaliableMaintence')
api.add_resource(doctorAPI, '/getDoctors')
api.add_resource(nurseAPI, '/getNurses')
api.add_resource(patientAPI, '/getPatients')
api.add_resource(medicationAPI, '/getMedications')
api.add_resource(prescribedMedsAPI, '/getprescribedmeds')
api.add_resource(MaintenceAPI, '/maintenceAPI_given_h_name')
api.add_resource(getRooms, '/getRooms')
api.add_resource(nuresRoomJunc, '/nurse_room_junc')

@app.route('/')
def home():
    return 'hello'

if __name__ == '__main__':
    app.run(debug=True)