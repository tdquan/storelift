import uuid
import datetime

from app.main import db
from app.main.models.user import User

def save_new_user(data):
	new_user = User(
		public_id = str(uuid.uuid4()),
	)

	if save_changes(new_user):
		response = {
			'status': 'success',
			'message': 'User created'
		}

		return response, 201
	else:
		response = {
			'status': 'fail',
			'message': 'Failed to create user'
		}

		return response, 409

def get_all_users():
	return User.query.all()

def find_user(public_id):
	return User.query.filter_by(public_id=public_id).first()

def save_changes(data):
	committed = True
	db.session.add(data)
	try:
		db.session.commit()
	except Exception as e:
		print(e)
		db.session.rollback()
		db.session.flush()
		committed = False

	return committed
