from cerberus import Validator
from flask import abort
from payloads.payload import Payload
from responses.response import Response
from exceptions.country_exception import CountryException

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

        self.validateCountries()
    
    def validateCountries(self):
        first_country = self.data['first_country']
        second_country = self.data['second_country']

        if (first_country.upper() == second_country.upper()) :
            raise CountryException('The countries cannot be the same.')
