import uuid
from datetime import datetime

from app.main import db
from app.main.models.user import User
from .shared import save

class UserService:
	""" User-related operations """

	def create_user(self, data):
		new_user = User(
			public_id = str(uuid.uuid4()),
			email = data['email']
		)

		if save(new_user):
			response = {
				'status': 'success',
				'message': 'User created'
			}
			return response, 201
		else:
			response = {
				'status': 'failure',
				'message': 'Failed to create user'
			}
			return response, 409

	def all_users(self):
		return User.query.all()

	def find_user(self, public_id):
		return User.query.filter_by(public_id=public_id).first()
