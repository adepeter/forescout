import os
import requests

from flask import Flask, redirect
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)


class ARPListAPI(Resource):
    def get(self):
        api_url = os.getenv('APIURL', 'http://127.0.0.1:8000')
        arp_url = f'{api_url}/v1/arps/'
        try:
            session = requests.Session()
            session.trust_env = False
            response = session.get(arp_url)
            if response.status_code == 200:
                return response.json()
        except Exception:
            return {'message': 'Error'}, 404


@app.route('/')
def home():
    return redirect('/v1/arps')

api.add_resource(ARPListAPI, '/v1/arps', endpoint='arps')
