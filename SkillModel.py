from os import error
from flask import Flask
# Import sql alchemy
from flask_sqlalchemy import SQLAlchemy
import json
from settings import app

# Creating the object of the database class
db = SQLAlchemy(app)

class Book(db.Model):
    # Defining the table name
    __tablename__ = 'skills'
        # Defining columns
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(80), nullable = False)
    price = db.Column(db.Float, nullable = False)
    isbn = db.Column(db.Integer)

