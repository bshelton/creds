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


class System(db.Model):
    __tablename__ = 'system'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False)
    environment = db.Column(db.String(30), db.ForeignKey('environment.id'), nullable=False)

    def __init__(self, name, environment):
        self.name = name
        self.environment = environment

class Environment(db.Model):
    __tablename__ = 'environment'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False)

    def __init__(self, name):
        self.name = name

class Service(db.Model):
    __tablename__ = 'service'
    id = db.Column(db.Integer, primary_key=True)
    host = db.Column(db.String(50), nullable=False)
    port = db.Column(db.Integer, nullable=False)
    system_id = db.Column(db.Integer, db.ForeignKey('system.id'), nullable=False)

    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.system_id = system_id

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