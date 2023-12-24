from flask import Flask, request, jsonify
from flask_cors import CORS
from payloads.get_relationship_payload import ValidateRelationshipPayload
from payloads.payload import Payload
from resources.relationship_get_resource import RelationshipGetResource
from exceptions.country_exception import CountryException

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "http://localhost:8080"}})

@app.route("/")
def get_relationship(): 
    request_data = Payload.format_request_data(request)
    ValidateRelationshipPayload(request_data).validate()
    return RelationshipGetResource(request_data).execute()

@app.errorhandler(400)
def generic_error(errors):
    print(errors.description)
    return jsonify({"errors": errors.description})

@app.errorhandler(500)
def internal_error(error):
    print(error.description)
    return jsonify({"errors": [error.description]})

@app.errorhandler(CountryException)
def handle_bad_request(e):
    return jsonify({"errors": [
        e.message
    ]}), 400

if __name__ == '__main__':
    app.run(debug=True)
    