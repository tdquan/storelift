import uuid
from random import random, randint

from app.main import db
from app.main.models.product import Product

class ProductService:
	""" Product related operations """

	def create_product(self, data):
		public_id = str(uuid.uuid4())
		price = data['price']
		name = data['name']
		product = Product(name=name, price=price, public_id=public_id)
		if self.save(product):
			response = { 'status': 'success', 'message': 'Product created' }
			return response, 201
		else:
			response = { 'status': 'failure', 'message': 'Failed to create product' }
			return response, 409

	def all_products(self):
		return Product.query.all()

	def find_product(self, public_id):
		return Product.query.filter_by(public_id=public_id)

	def save(self, data):
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
