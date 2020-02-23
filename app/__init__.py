from flask_restplus import Api
from flask import Blueprint

from app.main.controllers.products_controller import api as product_ns

blueprint = Blueprint('api', __name__)

api = Api(
	blueprint,
	title='STORELIFT API',
	version='0.1.0',
	description='Api for store actions'
)

api.add_namespace(product_ns, path='/products')
