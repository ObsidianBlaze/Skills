from os import error
from flask import Flask
# Import sql alchemy
from flask_sqlalchemy import SQLAlchemy
import json
from settings import app

# Creating the object of the database class
db = SQLAlchemy(app)

# Language model
class Language(db.Model):
    # Defining the table name
    __tablename__ = 'language'
        # Defining columns
    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    name = db.Column(db.String(80), nullable = False)
    # Reference to the foreign key being created
    profession_industries = db.relationship('Profession_Industries', backref = 'language', cascade = 'all, delete-orphan', lazy = 'dynamic')
    major_organizations = db.relationship('Major_Organizations', backref = 'language', cascade = 'all, delete-orphan', lazy = 'dynamic')
    specialization = db.relationship('Specialization', backref = 'language', cascade = 'all, delete-orphan', lazy = 'dynamic')


#Profession_Industries model
class Profession_Industries(db.Model):
    # Defining the table name
    __tablename__ = 'profession_Industries'
        # Defining columns
    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
# Linking with a foreign key
    language_id = db.Column(db.Integer, db.ForeignKey('language.id'), nullable = False)
    profession = db.Column(db.String(150), nullable = False)


#Major_organization model
class Major_Organizations(db.Model):
    # Defining the table name
    __tablename__ = 'major_organizations'
        # Defining columns
    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
# Linking with a foreign key
    language_id = db.Column(db.Integer, db.ForeignKey('language.id'), nullable = False)
    organization_name = db.Column(db.String(150), nullable = False)

#Specializations
class Specialization(db.Model):
    # Defining the table name
    __tablename__ = 'specialization'
        # Defining columns
    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
# Linking with a foreign key
    language_id = db.Column(db.Integer, db.ForeignKey('language.id'), nullable = False)
    specialization = db.Column(db.String(150), nullable = False)
