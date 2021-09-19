from os import error
from flask import Flask
# Import sql alchemy
from flask_sqlalchemy import SQLAlchemy
import json

from werkzeug.datastructures import LanguageAccept
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

    # Adding a language
    def add_langauge(_name):
        newLanguage = Language(name = _name)
        # Adding the language to the session
        db.session.add(newLanguage)

        # Committing the language to the database
        db.session.commit()

    # Getting all languages
    def get_all_languages():
        return Language.query.all()

    # Beautifying the structure of the output
    def __repr__(self):
        language_object = {
            'name': self.name
        }
        # Changing the dictionary to json
        return json.dumps(language_object)


#Profession_Industries model
class Profession_Industries(db.Model):
    # Defining the table name
    __tablename__ = 'profession_Industries'
        # Defining columns
    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
# Linking with a foreign key
    language_id = db.Column(db.Integer, db.ForeignKey('language.id'), nullable = False)
    profession = db.Column(db.String(150), nullable = False)

    # Adding a profession
    def add_profession(_language_id, _profession):
        newProfession = Profession_Industries(language_id = _language_id, profession = _profession)
        # Adding the profession to the session
        db.session.add(newProfession)

        # Committing the profession to the database
        db.session.commit()

    # Getting all professions
    def get_all_professions():
        return Profession_Industries.query.all()

    # Beautifying the structure of the output
    def __repr__(self):
        profession_object = {
            'language_id': self.language_id,
            'profession': self.profession
        }
        # Changing the dictionary to json
        return json.dumps(profession_object)



#Major_organization model
class Major_Organizations(db.Model):
    # Defining the table name
    __tablename__ = 'major_organizations'
        # Defining columns
    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
# Linking with a foreign key
    language_id = db.Column(db.Integer, db.ForeignKey('language.id'), nullable = False)
    organization_name = db.Column(db.String(150), nullable = False)

    # Adding an orgainization
    def add_organization(_language_id, _organization_name):
        newMajorOrganization = Major_Organizations(language_id = _language_id, organization_name = _organization_name)
        # Adding the orgainization to the session
        db.session.add(newMajorOrganization)

        # Committing the orgainization to the database
        db.session.commit()

    # Getting all major orgainizations
    def get_all_organizations():
        return Major_Organizations.query.all()

    # Beautifying the structure of the output
    def __repr__(self):
        organization_object = {
            'language_id': self.language_id,
            'organization_name': self.organization_name
        }
        # Changing the dictionary to json
        return json.dumps(organization_object)





#Specializations
class Specialization(db.Model):
    # Defining the table name
    __tablename__ = 'specialization'
        # Defining columns
    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
# Linking with a foreign key
    language_id = db.Column(db.Integer, db.ForeignKey('language.id'), nullable = False)
    specialization = db.Column(db.String(150), nullable = False)
