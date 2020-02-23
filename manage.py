import os
import unittest

from flask_script import Manager, Shell
from flask_migrate import Migrate, MigrateCommand

from app import blueprint
from app.main import create_app, db
from app.main.models import user, visit, cart, product
from app.main import models

app = create_app(os.getenv('BOILERPLATE_ENV') or 'dev')
app.register_blueprint(blueprint)

app.app_context().push()

manager = Manager(app)

migrate = Migrate(app, db)

def _make_context():
	return dict(app=app, db=db, models=models)

manager.add_command('db', MigrateCommand)
manager.add_command("shell", Shell(make_context=_make_context))

@manager.command
def run():
	app.run(host=app.config.get("HOST", "localhost"))

@manager.command
def test():
	"""Run the unit tests."""
	tests = unittest.TestLoader().discover('app/tests', pattern='test*.py')
	result = unittest.TextTestRunner(verbosity=2).run(tests)
	if result.wasSuccessful():
		return 0
	return 1

if __name__ == '__main__':
	manager.run()
