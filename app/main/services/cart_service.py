import uuid
from datetime import datetime

from app.main import db
from app.main.models.cart import Cart
from .shared import save

class CartService:
	""" Cart-related operations """

	def create_cart(self, data):
		cart = Cart(
			public_id = str(uuid.uuid4()),
			visit_id = data['visit_id']
		)

		if save(cart):
			return cart
		else:
			return None

	def find_cart(self, public_id):
		return Cart.query.filter_by(public_id=public_id).first()

	def all_carts(self):
		return Cart.query.all()

	def add_to_cart(self, cart, product):
		existing = self.check_existing_product(cart, product)
		if existing:
			response = {
				'status': 'failure',
				'message': 'Product already added to the cart'
			}

			return response, 409
		else:
			cart.total += product.price
			product.cart_id = cart.id
			save(cart)
			save(product)
			response = {
				'status': 'success',
				'message': 'Product added to the cart. Total is {total}'.format(total=cart.total)
			}

			return response, 200

	def remove_from_cart(self, cart, product):
		existing = self.check_existing_product(cart, product)
		if existing:
			cart.total -= product.price
			product.cart_id = None
			save(cart)
			save(product)
			response = {
				'status': 'success',
				'message': 'Product removed from the cart. Total is {total}'.format(total=cart.total)
			}

			return response, 200
		else:
			response = {
				'status': 'not found',
				'message': 'There is no such product in the cart'
			}
			return response, 404

	def check_existing_product(self, cart, product):
		return cart.products.filter_by(public_id=product.public_id).first()
