from api import db
from datetime import datetime

class Users(db.Model):
     __tablename__ = 'users'
     id = db.Column(db.Integer, primary_key=True)
     username = db.Column(db.String(255))
     password = db.Column(db.String(2323))

     def __init__(self, username, password):
        self.username = username
        self.password = password


class Service(db.Model):
    __tablename__ = 'service'
    id = db.Column(db.Integer, primary_key=True)
    host = db.Column(db.String(50), nullable=False)
    port = db.Column(db.Integer, nullable=False)

    def __init__(self, host, port):
        self.host = host
        self.port = port

class Account(db.Model):
    __tablename__ = 'account'
    id = db.Column(db.Integer, primary_key=True)
    created = db.Column(db.DateTime)
    user = db.Column(db.String(40), nullable=False)
    password = db.Column(db.String(2555), nullable=False)
    service_id = db.Column(db.Integer, db.ForeignKey('service.id'))

    def __init__(self, created, user, password, service_id):
        self.created = created
        self.user = user
        self.password = password
        self.service_id = service_id