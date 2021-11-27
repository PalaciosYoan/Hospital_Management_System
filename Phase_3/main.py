from db_packages.Data_Base_Manager import Data_Base_Manager
from flask import Flask, render_template, jsonify, request, redirect, session, g
from flask_restful import Api, Resource
from flask.helpers import url_for
from distutils.log import error
import json

app = Flask(__name__)
api = Api(app)
db_manager = Data_Base_Manager()

class getHospitalData(Resource):
    def get(self):
        df = db_manager.get_hospitals()
        json_data = json.loads(df.to_json())
        return json_data

api.add_resource(getHospitalData, '/gethospital')

@app.route('/')
def home():
    return 'hello'

if __name__ == '__main__':
    app.run(debug=True)
