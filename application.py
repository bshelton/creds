from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import model
import settings as settings

def create_app():
    app = Flask(__name__)
    app.config.from_object(settings)
    db = SQLAlchemy(app)
    
    return app
