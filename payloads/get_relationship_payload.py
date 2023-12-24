from cerberus import Validator
from flask import abort
from payloads.payload import Payload
from responses.response import Response
from exceptions.country_exception import CountryException
from dotenv import load_dotenv
import os
import requests

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

        first_country_api_url = "{the_api_url}/name/{country_name}".format(
            the_api_url = os.environ.get('REST_COUNTRIES_API_URL'), 
            country_name = first_country.lower()
        )
        first_country_data = requests.get(first_country_api_url)

        if (first_country_data.status_code != 200):
            raise CountryException('The first country doesn\'t exist!')

        second_country_api_url = "{the_api_url}/name/{country_name}".format(
            the_api_url = os.environ.get('REST_COUNTRIES_API_URL'), 
            country_name = second_country.lower()
        )
        second_country_data = requests.get(second_country_api_url)

        if (second_country_data.status_code != 200):
            raise CountryException('The second country doesn\'t exist!')