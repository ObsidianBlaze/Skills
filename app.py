from flask import Flask, json, jsonify, request, Response
from settings import *

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


# Used to show error messages
if __name__ == "__main__":
    app.run(debug=True)

# Starting the server for the application on port 5000
app.run(port=5000)
