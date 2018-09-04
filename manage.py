
import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from api import app, db

from flask_script import Manager, Server
from application import create_app
from flask_migrate import MigrateCommand

manager = Manager(app)
manager.add_command('db', MigrateCommand)

@manager.command
def create_all_db():
    db.create_all()

manager.add_command("runserver", Server(
    use_debugger=True,
    use_reloader=True,
    host=os.getenv('IP', '0.0.0.0'),
    port=int(os.getenv('PORT', 5555)))
)

if __name__ == "__main__":
    manager.run()
