from flask import Flask, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os, sys

sys.path.append('/home/brock/api')


import settings as settings

app = Flask(__name__)
app.config.from_object(settings)

db = SQLAlchemy(app)

migrate = Migrate(app, db)

import views
import model

if __name__ == '__main__':
    app.run()