class Payload:
    def __init__(self, data):
        self.data = data
    
    @staticmethod
    def format_request_data(data):
        payload = {
            'method': data.method
        }

        for arg in data.args:
            payload[arg] = data.args[arg]

        return payload
    
    def country_validator(self, field, value, error):
        # Special chars validator
        special_characters = "!@#$%^&*()_+={}[]|\:;'<>,.?/~`"
        if any(char in special_characters for char in value):
            error(field, "Contains special characters")

        # Has empty value
        if not value:
            error(field, "Is empty")

        # Has numbers
        special_characters = "0123456789"
        if any(char in special_characters for char in value):
            error(field, "Contains numbers")