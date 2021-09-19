from os import error
from flask import Flask
# Import sql alchemy
from flask_sqlalchemy import SQLAlchemy
import json
from settings import app

# Creating the object of the database class
db = SQLAlchemy(app)

# Language model
class Book(db.Model):
    # Defining the table name
    __tablename__ = 'language'
        # Defining columns
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(80), nullable = False)

#Profession_Industries model
class Book(db.Model):
    # Defining the table name
    __tablename__ = 'profession_Industries'
        # Defining columns
    id = db.Column(db.Integer, primary_key = True)
    language_id = db.Column(db.Integer, nullable = False)
    profession = db.Column(db.String(150), nullable = False)

#Major_organization model
class Book(db.Model):
    # Defining the table name
    __tablename__ = 'major_organizations'
        # Defining columns
    id = db.Column(db.Integer, primary_key = True)
    language_id = db.Column(db.Integer, nullable = False)
    organization_name = db.Column(db.String(150), nullable = False)

#Specializations
class Book(db.Model):
    # Defining the table name
    __tablename__ = 'specialization'
        # Defining columns
    id = db.Column(db.Integer, primary_key = True)
    language_id = db.Column(db.Integer, nullable = False)
    specialization = db.Column(db.String(150), nullable = False)
