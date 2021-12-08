from numpy import delete
from db_packages.Data_Base_Manager import Data_Base_Manager
from flask import Flask, render_template, jsonify, request, redirect, session, g
from flask_restful import Api, Resource
from flask.helpers import url_for
from distutils.log import error
from flask_cors import CORS
import pandas as pd
import json


query = """
                select * from Maintenance where maint_id = "{}";
            """.format(name)
# self.cursor.execute(query, (name))
# rows = self.cursor.fetchall()
# df = pd.DataFrame(columns=['maint_id', 'name', 'started_working', 'duty', 'phone_number'])
# for row in rows:
#     df = df.append({
#             'maint_id':row[0], 'name':row[1], 
#             'started_working':row[2], 'duty':row[3],
#             'phone_number':row[4]})
df = pd.read_sql_query(query, con=self.conn)