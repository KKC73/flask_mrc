import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from flask import Flask
from flask_restful import Resource, Api, reqparse
import pandas as pd
import ast

# Fetch the service account key JSON file contents
cred = credentials.Certificate('mekong-6edd6-firebase-adminsdk-14sqd-df1a18f32f.json')
# Initialize the app with a service account, granting admin privileges
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://mekong-6edd6-default-rtdb.firebaseio.com'
})

ref = db.reference('/')

ref = db.reference('boxes')

app = Flask(__name__)
api = Api(app)

class MRC(Resource):
    def get(self):
        return ref.get(), 200  # return data and 200 OK

api.add_resource(MRC, '/mrc')  # add endpoints

if __name__ == '__main__':
    app.run()  # run our Flask app