from resources.resource import Resource

class RelationshipGetResource(Resource):
    def __init__(self, data):
        Resource.__init__(self, data)
    
    def execute(self):
        return self.data