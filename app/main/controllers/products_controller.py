from flask import request
from flask_restplus import Resource

from app.main.utils.dto import ProductDto
from app.main.services.product_service import ProductService

api = ProductDto.api
_product = ProductDto.product
service = ProductService()

@api.route('/', strict_slashes=False)
class ProductList(Resource):
	@api.doc('List of all products')
	@api.marshal_with(_product, envelope='data')
	def get(self):
		""" List all products """
		return service.all_products()

	@api.response(201, 'Product created')
	@api.response(409, 'Failed to create product')
	@api.doc('Create a new product')
	@api.expect(_product, validate=True)
	def post(self):
		""" Create a new product """
		data = request.json
		return service.create_product(data)
