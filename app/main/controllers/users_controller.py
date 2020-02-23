from flask import request
from flask_restplus import Resource

from app.main.utils.dto import UserDTO
from app.main.services.user_service import UserService

api = UserDTO.api
_user = UserDTO.user
service = UserService()

@api.route('/', strict_slashes=False)
class Users(Resource):
	@api.doc('List all users')
	@api.marshal_list_with(_user, envelope='data')
	def get(self):
		""" List all users """
		return service.all_users()

	@api.doc('Creating a new user')
	@api.response(201, 'User created')
	@api.response(409, 'Failed to create user')
	@api.expect(_user, validate=True)
	def post(self):
		""" Create a new user """
		data = request.json
		return service.create_user(data)
