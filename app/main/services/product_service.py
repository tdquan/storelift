import uuid
from random import random, randint

from app.main.models.product import Product
from .shared import save

class ProductService:
	""" Product related operations """

	def create_product(self, data):
		product = Product(
			public_id = str(uuid.uuid4()),
			name = data['name'],
			price = data['price']
		)

		if save(product):
			response = {
				'status': 'success',
				'message': 'Product created'
			}
			return response, 201
		else:
			response = {
				'status': 'failure',
				'message': 'Failed to create product'
			}
			return response, 409

	def all_products(self):
		return Product.query.all()

	def find_product(self, public_id):
		return Product.query.filter_by(public_id=public_id).first()
