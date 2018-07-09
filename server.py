from flask import Flask, jsonify
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

counter = 0

class res_one(Resource):
    def get(self):
        return jsonify(endpoint='res_one', method='GET', counter=counter)

    def post(self):
        global counter
        counter += 1

api.add_resource(res_one, '/res_one')

app.run(port=5001)