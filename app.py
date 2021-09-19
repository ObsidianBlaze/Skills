from flask import Flask, json, jsonify, request, Response
from settings import *

@app.route('/')
def hello_world():
    return "Hello World!"



# Used to show error messages
if __name__ == "__main__":
      app.run(debug=True)

# Starting the server for the application on port 5000
app.run(port=5000)
