from flask import request
from flask_restplus import Resource

from app.main.utils.dto import UserDTO
from app.main.services.user_service import UserService
from app.main.services.visit_service import VisitService

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

@api.route('/<public_id>')
@api.param('public_id', 'User\'s identifier')
@api.response(404, 'User not found')
class User(Resource):
	@api.doc('Get an user given his identifier')
	@api.marshal_with(_user)
	def get(self, public_id):
		""" Get an user given his identifier """
		user = service.find_user(public_id)
		if not user:
			api.abort(404, 'User with id {public_id} cannot be found'.format(public_id=public_id))
		else:
			return user

@api.route('/<public_id>/enter')
@api.param('public_id', 'User\'s identifier')
@api.response(404, 'User not found')
@api.response(201, 'User entered store')
class UserEnters(Resource):
	@api.doc('Processes that happen when an user enters a store')
	def post(self):
		""" Automatically create a new visit and cart when an user enters a store """
		user = service.find_user(public_id)
		if not user:
			api.abort(404, 'User with id {public_id} cannot be found'.format(public_id=public_id))

		visit = visit_service.create_visit({ 'user_id': user.id })

