import sqlite3
from db import db


#the app uses the model of the resource, not the actual resource.
class UserModel(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80))
    password = db.Column(db.String(80))


    def __init__(self, username, password):
        
        self.username = username
        self.password = password

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    #2 mapping methods
    @classmethod
    def find_by_username(cls, username):
        return cls.query.filter_by(username=username).first()

    @classmethod
    def find_by_id(cls, _id):
        return cls.query.filter_by(id=_id).first()

    #usermodel is an API. Not a REST API.
    #exposes 2 endpoints/methods. find_by_username, find_by_id.
    #security.py uses them. implementation changed but interface didnt change
    #no change needed in security.py.
