import os
import requests

from flask import Flask, redirect
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)


class ARPListAPI(Resource):
    def get(self):
        api_url = 'http://collector:8000'
        arp_url = f'{api_url}/v1/arps/'
        try:
            response = requests.get(arp_url)
            if response.status_code == 200:
                return response.json()
        except Exception:
            return {'message': 'Error'}, 404


@app.route('/')
def home():
    return redirect('/v1/arps')

api.add_resource(ARPListAPI, '/v1/arpss', endpoint='arps')
