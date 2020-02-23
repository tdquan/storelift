from flask_restplus import Namespace, fields

class UserDTO:
	api = Namespace('users', description='user-related data')
	user = api.model('user', {
		'email': fields.String(description='user\'s email'),
		'public_id': fields.String(description='user\'s identifier')
	})

class ProductDTO:
	api = Namespace('products', description='product-related data')
	product = api.model('product', {
		'public_id': fields.String(description='product public identifier'),
		'name': fields.String(required=True, description='name of product'),
		'price': fields.Integer(required=True, description='price of product'),
		'cart_id': fields.Integer(description='cart_id of the cart that buys the product')
	})

class VisitDTO:
	api = Namespace('visits', description='visit-related data')
	visit = api.model('visit', {
		'public_id': fields.String(description='visit\'s public identifier'),
		'enter_time': fields.DateTime(required=True, description='time of visit'),
		'exit_time': fields.DateTime(description='time visit ends'),
		'user_id': fields.Integer(required=True, description='id of the visitor')
	})

class CartDTO:
	api = Namespace('carts', description='cart-related data')
	cart = api.model('cart', {
		'public_id': fields.String(description='cart\'s public identifier'),
		'total': fields.Integer(required=True, description='total price of all products'),
		'visit_id': fields.Integer(required=True, description='id of the visit'),
		'checked_out': fields.Boolean(description='status if the cart is paid for')
	})
