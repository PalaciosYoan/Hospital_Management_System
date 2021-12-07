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
        action = json.loads(request.data)['queryType']
        if action == 'maint_name':
            maint_name = json.loads(request.data)['maint_name']
            df = db_manager.get_hospital_given_maintence(maint_name=maint_name)
            df = df.to_dict('records')
            return df
        elif action == 'post':
            data = json.loads(request.data)
            h_name = data['name']
            address = data['address']
            db_manager.insert_hospital(h_name, address)
            
    def delete(self):
        h_id = json.loads(request.data)['h_id']
        db_manager.delete_hospital(h_id=h_id)
class avaliableMaintenceAPI(Resource):
    def post(self):
        #must send a json format {'hospital_name':hospital_name}
        hospital_name = json.loads(request.data)['hospital_name']
        df = db_manager.get_avaliable_maintence(hospital_name)
        df = df.to_dict('records')
        return df

class MaintenceAPI(Resource):
    def post(self):
        #must send a json format {'hospital_name':hospital_name}
        action = json.loads(request.data)['queryType']
        if action == 'get':
            hospital_name = json.loads(request.data)['hospital_name']
            df = db_manager.get_maintenance_given_hospital(hospital_name)
            df = df.to_dict('records')
            return df
        elif action == 'post-junction-table':
            data = json.loads(request.data)
            h_name = data['hospital_name']
            maint_name = data['maintenance_name']
            db_manager.insert_specific_maintenance_hos_junct(h_name, maint_name)
            return 'status: 200'
        elif action =='insert-maintenance': # easily be able to add more queries to doctor
            data = json.loads(request.data)
            name = data['maint_name']
            started_working = data['start_date']
            phone_number = data['phone_number']
            duty = data['duty']
            db_manager.insert_maint(name, started_working, phone_number, duty)

    def delete(self):
        given = json.loads(request.data)
        if given['queryType'] == "junctionTable":
            h_name = given['hospital_name']
            maint_name = given['maintenance_name']
            db_manager.delete_specific_maintenance_junc_hos(h_name, maint_name)
            return
        if given['queryType'] == "maintTable":
            maint_name = given['maintenance_name']
            db_manager.delete_specific_maintenance(maint_name=maint_name)
            return
    
class doctorAPI(Resource):
    def post(self):
        action = json.loads(request.data)['queryType']
        if action == 'hospital':
            hospital_name = json.loads(request.data)['hospital_name']
            df = db_manager.get_doctors_given_hospital(hospital_name)
            df = df.to_dict('records')
            return df
        elif action =='insert-doctor': # easily be able to add more queries to doctor
            data = json.loads(request.data)
            name = data['doctor_name']
            started_working = data['start_date']
            phone_number = data['phone_number']
            h_name = data['hospital_name']
            db_manager.insert_doctor(name, started_working, phone_number, h_name)
        elif action =='hospital-doctor': # easily be able to add more queries to doctor
            data = json.loads(request.data)
            hos_name = data['doctor_name']
            doc_name = data['hospital_name']
            df = db_manager.get_doctors_given_hospital_doc_name(hos_name, doc_name)
            df = df.to_dict('records')
            return df
        
    def delete(self):
        data = json.loads(request.data)
        doc_name = data['doctor_name']
        db_manager.delete_doctor(doc_name=doc_name)

class nurseAPI(Resource):
    def post(self):
        action = json.loads(request.data)['queryType']
        if action == 'hospital':
            hospital_name = json.loads(request.data)['hospital_name']
            df = db_manager.get_nurses_given_hospital(hospital_name)
            df = df.to_dict('records')
            return df
        elif action == "room":
            r_number = json.loads(request.data)["room_number"]
            h_name = json.loads(request.data)["hospital_name"]
            df = db_manager.get_nurses_given_rooms(r_number=r_number, h_name=h_name)
            df = df.to_dict('records')
            return df
        elif action =='insert-nurse': # easily be able to add more queries to doctor
            data = json.loads(request.data)
            name = data['nurse_name']
            started_working = data['start_date']
            phone_number = data['phone_number']
            h_name = data['hospital_name']
            db_manager.insert_nurse(name, started_working, phone_number, h_name)
        elif action == 'nurse-hospital':
            data = json.loads(request.data)
            hospital_name = data['hospital_name']
            nurse_name = data['nurse_name']
            df = db_manager.get_nurse_given_hospital_nurse_name(hospital_name, nurse_name)
            df = df.to_dict('records')
            return df 
    
    def delete(self):
        data = json.loads(request.data)
        n_name = data['nurse_name']
        db_manager.delete_nurse(n_name=n_name)

class patientAPI(Resource):
    def post(self):
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
    def delete(self):
        data = json.loads(request.data)
        p_name = data['patient_name']
        dob = data['dob']
        db_manager.delete_patient(p_name=p_name, dob=dob)
        
    def put(self):
        action = json.loads(request.data)['queryType']
        if action == 'released_date':
            data = json.loads(request.data)
            db_manager.update_released_date(data['released_date'], data['patient_name'], data['dob'])
            
        elif action == 'update_doctor':
            data = json.loads(request.data)
            db_manager.update_released_date(data['doctor_name'], data['patient_name'], data['dob'])
            
        return "Success 200"


class medicationAPI(Resource):
    def post(self):
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
        elif action =='post':
            json_data = json.loads(request.data)
            m_name = json_data['medication_name']
            h_name = json_data['hospital_name']
            cost = json_data['cost']
            type = json_data['type']
            side_effect = json_data['side_effect']
            treament_for = json_data['treament_for']
            db_manager.insert_specific_medication(m_name, h_name, cost, type, side_effect, treament_for)
            return 'status: 200'
        elif action == 'hospital-med':
            json_data = json.loads(request.data)
            m_name = json_data['medication_name']
            h_name = json_data['hospital_name']
            df = db_manager.get_medication_given_hospital_med_name(h_name, m_name)
            df = df.to_dict('records')
            return df
        
    def delete(self):
        hospital_name = json.loads(request.data)['hospital_name']
        m_name = json.loads(request.data)['medication_name']
        db_manager.delete_specific_medication(m_name, hospital_name)
        return 'status: 200'
class getRooms(Resource):
    def get(self):
        return db_manager.get_rooms_not_filled()
    
    def post(self):
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
            hospital_id = json.loads(request.data)['hospital_id']
            return db_manager.get_rooms_not_filled(hospital_id)
        
class getMaintenanceListForAHospital(Resource):
    def post(self):
        hospital_name = json.loads(request.data)['hospital_name']
        df = db_manager.get_maintenance_given_hospital(hospital_name)
        df = df.to_dict('records')
        return df
    

class prescribedMedsAPI(Resource):
    def post(self):
        action = json.loads(request.data)['queryType']
        if action == 'get':
            patient_name = json.loads(request.data)['patient_name']
            dob = json.loads(request.data)['dob']
            df = db_manager.get_medication_given_patient(patient_name, dob)
            df = df.to_dict('records')
            return df
        elif action == 'post':
            data = json.loads(request.data)
            assigned_date = data['assigned_date']
            p_name = data['patient_name']
            m_name = data['medication_name']
            h_name = data['hospital_name']
            dob = data['dob']
            db_manager.insert_specific_prescribed_med(assigned_date, p_name, dob, m_name, h_name)
            return 'status: 200'
    
    def delete(self):
        data = json.loads(request.data)
        patient_name = data['patient_name']
        dob = data['dob']
        hospital_name = data['hospital_name']
        med_name = data['medication_name']
        db_manager.delete_specific_prescribed_med(dob=dob, p_name=patient_name, med_name=med_name, h_name = hospital_name)
        return 'status: 200'
    
class nuresRoomJunc(Resource):
    def post(self):
        data = json.loads(request.data)
        n_id = data['n_id']
        r_id = data['r_id']
        assign_date = data['assigned_date']
        db_manager.insert_nurse_room_junction(n_id, r_id, assign_date)
    
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