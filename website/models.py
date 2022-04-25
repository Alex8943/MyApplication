from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func

class Note(db.Model): 
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(10000))
    date = db.Column(db.DateTime(timezone=True), default= func.now()) 
    #Flash will set todays date automatic for us, when i create a note. 

    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    #OneToMany relationship, one user can have many notes

class User(db.Model, UserMixin):
    #Dessigning schema for our database
    id = db.Column(db.Integer, primary_key=True) #Id is primary key
    email = db.Column(db.String(150), unique = True)
    firstname = db.Column(db.String(150))
    password = db.Column(db.String(150))

    notes = db.relationship('Note')