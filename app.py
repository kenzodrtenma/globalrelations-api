from flask import Flask, request, jsonify
from payloads.get_relationship_payload import ValidateRelationshipPayload
from payloads.payload import Payload
from resources.relationship_get_resource import RelationshipGetResource

app = Flask(__name__)

@app.route("/")
def get_relationship():
    request_data = Payload.format_request_data(request)
    ValidateRelationshipPayload(request_data).validate()
    return RelationshipGetResource(request_data).execute()

@app.errorhandler(400)
def generic_error(errors):
    print(errors.description)
    return jsonify({"errors": errors.description})

if __name__ == '__main__':
    app.run(debug=False)
    