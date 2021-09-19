from flask import Flask

# Creating the app object
app = Flask(__name__)

# Config to point to the location of the database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False