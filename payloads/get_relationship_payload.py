from cerberus import Validator
from flask import abort
from payloads.payload import Payload
from responses.response import Response

class ValidateRelationshipPayload(Payload):
    def __init__(self, data):
        Payload.__init__(self, data)

    def validate(self):
        schema = {
            'method': {
                'type': 'string',
                'allowed': [
                    'GET'
                ]
            },
            'first_country': {
                'type': 'string',
                'required': True,
                'validator': self.country_validator
            },
            'second_country': {
                'type': 'string',
                'required': True,
                'validator': self.country_validator
            }
        }
        
        v = Validator()
        valid_request = v.validate(self.data, schema)
        
        if (not valid_request):
            abort(400, Response.formatValidationErrors(v.errors))