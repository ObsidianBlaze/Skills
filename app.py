from flask import Flask, json, jsonify, request, Response
from settings import *

# Alternative dictionary in case database usage is not needed
skills = [{'python':
    {
        'name': 'The Cat In The Hat',
        'price': 6.99,
        'isbn': 123456789,

    }

}
]


# Route to get all skills
@app.route('/')
def getAllBooks():
    return jsonify({'skills': skills})


# Used to show error messages
if __name__ == "__main__":
    app.run(debug=True)

# Starting the server for the application on port 5000
app.run(port=5000)
