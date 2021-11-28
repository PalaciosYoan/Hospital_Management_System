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
        df = json.loads(df.to_json())
        return df
class hospitalAPI(Resource):
    def get(self):
        df = db_manager.get_hospitals()
        json_data = json.loads(df.to_json())
        return json_data

class avaliableMaintenceAPI(Resource):
    def get(self):
        #must send a json format {'hospital_name':hospital_name}
        hospital_name = json.loads(request.data)['hospital_name']
        df = db_manager.get_avaliable_maintence(hospital_name)
        json_data = json.loads(df.to_json())
        return json_data

class doctorAPI(Resource):
    def get(self):
        action = json.loads(request.data)['queryType']
        if action == 'hospital':
            hospital_name = json.loads(request.data)['hospital_name']
            df = db_manager.get_doctors_given_hospital(hospital_name)
            json_data = json.loads(df.to_json())
            return json_data
        #elif action =='' # easily be able to add more queries to doctor

class nurseAPI(Resource):
    def get(self):
        action = json.loads(request.data)['queryType']
        if action == 'hospital':
            hospital_name = json.loads(request.data)['hospital_name']
            df = db_manager.get_nurses_given_hospital(hospital_name)
            json_data = json.loads(df.to_json())
            return json_data

class patientAPI(Resource):
    def get(self):
        action = json.loads(request.data)['queryType']
        if action == 'hospital':
            hospital_name = json.loads(request.data)['hospital_name']
            df = db_manager.get_patients_given_hospital(hospital_name)
            json_data = json.loads(df.to_json())
            return json_data
        elif action == 'doctor':
            doctor_name = json.loads(request.data)['doctor_name']
            df = db_manager.get_patients_given_doctor(doctor_name)
            json_data = json.loads(df.to_json())
            return json_data
        elif action == 'nurse':
            nurse_name = json.loads(request.data)['nurse_name']
            df = db_manager.get_patients_given_nurse(nurse_name)
            json_data = json.loads(df.to_json())

class medicationAPI(Resource):
    def get(self):
        hospital_name = json.loads(request.data)['hospital_name']
        df = db_manager.get_medication_given_hospital(hospital_name)
        json_data = json.loads(df.to_json())
        return json_data

class getRooms(Resource):
    def get(self):
        action = json.loads(request.data)['queryType']
        if action == 'hospital':
            hospital_name = json.loads(request.data)['hospital_name']
            df = db_manager.get_rooms_given_hospital(hospital_name)
            json_data = json.loads(df.to_json())
            return json_data
        elif action == 'nurse':
            nurse_name = json.loads(request.data)['nurse_name']
            df = db_manager.get_rooms_given_nurse(nurse_name)
            json_data = json.loads(df.to_json())
class getMaintenanceListForAHospital(Resource):
    def get(self):
        hospital_name = json.loads(request.data)['hospital_name']
        df = db_manager.get_maintenance_given_hospital(hospital_name)
        json_data = json.loads(df.to_json())
        return json_data

class prescribedMedsAPI(Resource):
    def get(self):
        patient_name = json.loads(request.data)['patient_name']
        df = db_manager.get_maintenance_given_hospital(patient_name)
        json_data = json.loads(df.to_json())
        return json_data
    
api.add_resource(hospitalAPI, '/gethospital')
api.add_resource(allMaintenceAPI, '/getallMaintence')
api.add_resource(avaliableMaintenceAPI, '/getavaliableMaintence')
api.add_resource(doctorAPI, '/getDoctors')
api.add_resource(nurseAPI, '/getNurse')
api.add_resource(patientAPI, '/getPatients')
api.add_resource(medicationAPI, '/getMedications')
api.add_resource(prescribedMedsAPI, '/getprescribedmeds')

@app.route('/')
def home():
    return 'hello'

if __name__ == '__main__':
    app.run(debug=True)
