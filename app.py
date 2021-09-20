from flask import Flask, json, jsonify, request, Response
from settings import *
from SkillModel import *
import json

# Alternative dictionary in case database usage is not needed
skills = [
    # Adding dictionaries to hold the some book details
    {
        'name': 'Python',
        'profession': 'software engineer',
        'organization_name': 'Google',
        'specialization': 'desktop graphical user interfaces',

    },
    {
        'name': 'Java',
        'profession': 'Java developers',
        'organization_name': 'Eclipse Information Technologies',
        'specialization': 'Cloud Computing',

    }
]



# Route to get all skills
@app.route('/')
def getAllSkills():
    return jsonify({'skills': skills})

# Getting single language

@app.route('/language/<int:id>')
def getLanguage(id):
    return_value = Language.get_single_language(id)
    return jsonify(return_value)


# Used to show error messages
if __name__ == "__main__":
    app.run(debug=True)

# Starting the server for the application on port 5000
app.run(port=5000)
