from resources.resource import Resource
from openai import OpenAI

class RelationshipGetResource(Resource):
    def __init__(self, data):
        Resource.__init__(self, data)
    
    def execute(self):
        client = OpenAI()
        question = f"Summarize in one paragraph the current geopolitical relationship between the following countries: {self.data['first_country']} and {self.data['second_country']}. Your answer must be less than 375 characters."
        
        completion = client.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "Act like an expert in political science, history and geography. Your answers should contain a mixture of subject matter, wisdom, irreverence and touches of sarcasm."},
                {"role": "user", "content": question}
            ]
        )

        return {
            'in_a_few_words': completion.choices[0].message.content
        }