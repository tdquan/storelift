from flask import request
from flask_restplus import Resource

from app.main.utils.dto import ProductDTO
from app.main.services.product_service import ProductService

api = ProductDTO.api
_product = ProductDTO.product
service = ProductService()

@api.route('/', strict_slashes=False)
class Products(Resource):
	@api.doc('List of all products')
	@api.marshal_list_with(_product, envelope='data')
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

@api.route('/<public_id>')
@api.param('public_id', 'Product\'s identifier')
@api.response(404, 'Product not found')
class Product(Resource):
	@api.doc('Get a product\'s details')
	@api.marshal_with(_product)
	def get(self, public_id):
		""" Get a product given its identifier """
		product = service.find_product(public_id)
		if not product:
			api.abort(404, 'Product with id {public_id} cannot be found'.format(public_id=public_id))
		else:
			return product
