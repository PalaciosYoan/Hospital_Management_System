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
        maint_name = json.loads(request.data)['maint_name']
        df = db_manager.get_hospital_given_maintence(maint_name=maint_name)
        df = df.to_dict('records')
        return df

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
        elif action == 'post':
            data = json.loads(request.data)
            h_name = data['hospital_name']
            maint_name = data['maintenance_name']
            db_manager.insert_specific_maintenance(h_name, maint_name)
            return 'status: 200'

    def delete(self):
        data = json.loads(request.data)
        h_name = data['hospital_name']
        maint_name = data['maintenance_name']
        db_manager.delete_specific_maintenance(h_name, maint_name)
        return
    
class doctorAPI(Resource):
    def post(self):
        action = json.loads(request.data)['queryType']
        if action == 'hospital':
            hospital_name = json.loads(request.data)['hospital_name']
            df = db_manager.get_doctors_given_hospital(hospital_name)
            df = df.to_dict('records')
            return df
        #elif action =='' # easily be able to add more queries to doctor

class nurseAPI(Resource):
    def post(self):
        action = json.loads(request.data)['queryType']
        if action == 'hospital':
            hospital_name = json.loads(request.data)['hospital_name']
            df = db_manager.get_nurses_given_hospital(hospital_name)
            df = df.to_dict('records')
            return df

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

    def delete(self):
        hospital_name = json.loads(request.data)['hospital_name']
        m_name = json.loads(request.data)['medication_name']
        db_manager.delete_specific_medication(m_name, hospital_name)
        return 'status: 2000'
class getRooms(Resource):
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
            db_manager.insert_specific_prescribed_med(assigned_date, p_name, m_name, h_name)
            return 'status: 200'
    
    def delete(self):
        patient_name = json.loads(request.data)['patient_name']
        db_manager.delete_specific_prescribed_med(patient_name)
        return 'status: 200'
    
    
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

@app.route('/')
def home():
    return 'hello'

if __name__ == '__main__':
    app.run(debug=True)
