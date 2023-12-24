from resources.resource import Resource
from openai import OpenAI

class RelationshipGetResource(Resource):
    def __init__(self, data):
        Resource.__init__(self, data)
        self.mock = True
    
    def execute(self):

        if (self.mock):
            return {
                'relationship_status': 'Dynamic',
                'relationship_color': '#3498DB',
                'in_a_few_words': f"Summarize in one paragraph the current geopolitical relationship between the following countries: {self.data['first_country']} and {self.data['second_country']}. Your answer must be less than 375 characters."
            }
        
        client = OpenAI()
        
        relationship_status = client.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": self.system_behavior},
                {"role": "user", "content": f"Which adjective would best describe the relationship between the following countries: {self.data['first_country']} and {self.data['second_country']}. It should be a very peculiar word, very authentical, reply just with the adjective, and nothing more than this."},
            ]
        )

        relationship_color = client.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "user", "content": f"Select a color to represent the geopolitical relationship between these countries: {self.data['first_country']} and {self.data['second_country']}. Provide only a hexadecimal code as a response, including the #, and nothing more than that."},
            ]
        )

        few_words = client.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": self.system_behavior},
                {"role": "user", "content": f"Summarize in one paragraph the current geopolitical relationship between the following countries: {self.data['first_country']} and {self.data['second_country']}. Your answer must be less than 375 characters."}
            ]
        )

        return {
            'relationship_status': relationship_status.choices[0].message.content,
            'relationship_color': relationship_color.choices[0].message.content,
            'in_a_few_words': few_words.choices[0].message.content
        }