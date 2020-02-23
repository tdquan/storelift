from flask_restplus import Namespace, fields

class UserDto:
	api = Namespace('users', description='user related data operations')
	user = api.model('user', {
		'public_id': fields.String(required=True, description='user identifier')
	})

class ProductDto:
	api = Namespace('products', description='product related data operations')
	product = api.model('product', {
		'public_id': fields.String(description='product public identifier'),
		'name': fields.String(required=True, description='name of product'),
		'price': fields.Integer(required=True, description='price of product'),
		'cart_id': fields.Integer(description='cart_id of the cart that buys the product')
	})
