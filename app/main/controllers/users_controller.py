from flask import request
from flask_restplus import Resource

from app.main.utils.dto import UserDTO
from app.main.utils.dto import ProductDTO
from app.main.utils.dto import CartDTO
from app.main.services.user_service import UserService
from app.main.services.visit_service import VisitService
from app.main.services.cart_service import CartService
from app.main.services.product_service import ProductService

api = UserDTO.api
_user = UserDTO.user
_product = ProductDTO.product
_cart = CartDTO.cart
service = UserService()
visit_service = VisitService()
cart_service = CartService()
product_service = ProductService()

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
@api.response(201, 'User entered the store')
class UserEnters(Resource):
	@api.doc('Processes that happen when an user enters a store')
	def put(self, public_id):
		""" Automatically create a new visit and cart when an user enters a store """
		user = service.find_user(public_id)
		if not user:
			api.abort(404, 'User with id {public_id} cannot be found'.format(public_id=public_id))

		try:
			visit = visit_service.create_visit({ 'user_id': user.id })
			cart = cart_service.create_cart({ 'visit_id': visit.id })
			response = { 'status': 'success', 'message': 'user {public_id} entered store'.format(public_id=public_id) }
			return response, 201
		except Exception as e:
			print(e)
			response = { 'status': 'failure', 'message': 'some error occurred with user {public_id}'.format(public_id=public_id) }
			return response, 409

@api.route('/<public_id>/add_to_cart')
@api.param('public_id', 'User\'s identifier')
@api.response(404, 'User not found')
@api.response(409, 'Failed to add product to cart')
@api.response(200, 'Product added to cart')
@api.expect(_product, validate=True)
class UserAddToCart(Resource):
	@api.doc('User add a product to cart')
	def put(self, public_id):
		""" Add a product to cart """
		user = service.find_user(public_id)
		data = request.json
		if not user:
			api.abort(404, 'User with id {public_id} cannot be found'.format(public_id=public_id))

		try:
			visit = user.visits[-1]
			cart = visit.cart
			product = product_service.find_product(data['public_id'])
			return cart_service.add_to_cart(cart.public_id, product.public_id)
		except Exception as e:
			print(e)
			response = { 'status': 'failure', 'message': 'some error occurred when trying to add the product to the cart' }
			return response, 409

@api.route('/<public_id>/remove_from_cart')
@api.param('public_id', 'User\'s identifier')
@api.response(404, 'User not found')
@api.response(409, 'Failed to remove product from cart')
@api.response(200, 'Product removed from cart')
@api.expect(_product, validate=True)
class UserRemoveFromCart(Resource):
	@api.doc('User remove a product from the cart')
	def put(self, public_id):
		""" Remove a product from cart """
		user = service.find_user(public_id)
		data = request.json
		if not user:
			api.abort(404, 'User with id {public_id} cannot be found'.format(public_id=public_id))

		try:
			visit = user.visits[-1]
			cart = visit.cart
			product = product_service.find_product(data['public_id'])
			return cart_service.remove_from_cart(cart.public_id, product.public_id)
		except Exception as e:
			print(e)
			response = { 'status': 'failure', 'message': 'some error occurred when trying to remove the product from the cart' }
			return response, 409

@api.route('/<public_id>/check_out')
@api.param('public_id', 'User\'s identifier')
@api.response(404, 'User not found')
@api.response(409, 'Failed to check out items')
@api.response(200, 'User checked out')
@api.expect(_product, validate=True)
class UserCheckOut(Resource):
	@api.doc('User remove a product from the cart')
	def put(self, public_id):
		""" User check out """
		user = service.find_user(public_id)
		if not user:
			api.abort(404, 'User with id {public_id} cannot be found'.format(public_id=public_id))

		try:
			visit = user.visits[-1]
			cart = visit.cart
			return cart_service.check_out(cart.public_id)
		except Exception as e:
			print(e)
			response = { 'status': 'failure', 'message': 'some error occurred when user tried to checkout the cart' }
			return response, 409
