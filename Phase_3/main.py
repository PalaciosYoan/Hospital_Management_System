from db_packages.Data_Base_Manager import Data_Base_Manager
from flask import Flask, render_template, jsonify, request, redirect, session, g
from flask_restful import Api, Resource
from flask.helpers import url_for
from distutils.log import error
import json

app = Flask(__name__)
api = Api(app)
db_manager = Data_Base_Manager()

class getAllMaintence(Resource):
    def get(self):
        df = db_manager.get_maintence()
        df = json.loads(df.to_json())
        return df
class getHospitalData(Resource):
    def get(self):
        df = db_manager.get_hospitals()
        json_data = json.loads(df.to_json())
        return json_data

class getAvaliableMaintence(Resource):
    def get(self):
        #must send a json format {'hospital_name':hospital_name}
        hospital_name = json.loads(request.data)['hospital_name']
        df = db_manager.get_avaliable_maintence(hospital_name)
        json_data = json.loads(df.to_json())
        return json_data

class getDoctors(Resource):
    def get(self):
        action = json.loads(request.data)['queryType']
        if action == 'hospital':
            hospital_name = json.loads(request.data)['hospital_name']
            df = db_manager.get_avaliable_maintence(hospital_name)
            json_data = json.loads(df.to_json())
            return json_data
        #elif action =='' # easily be able to add more queries to doctor

class getNurse(Resource):
    def get(self):
        action = json.loads(request.data)['queryType']
        if action == 'hospital':
            hospital_name = json.loads(request.data)['hospital_name']
            df = db_manager.get_avaliable_maintence(hospital_name)
            json_data = json.loads(df.to_json())
            return json_data

api.add_resource(getHospitalData, '/gethospital')
api.add_resource(getAllMaintence, '/getAllMaintence')
api.add_resource(getAvaliableMaintence, '/AvaliableMaintence')
api.add_resource(getDoctors, '/getDoctors')
api.add_resource(getNurse, '/getNurse')

@app.route('/')
def home():
    return 'hello'

if __name__ == '__main__':
    app.run(debug=True)
