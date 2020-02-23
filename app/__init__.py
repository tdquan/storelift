from flask_restplus import Api
from flask import Blueprint

from app.main.controllers.users_controller import api as user_ns
from app.main.controllers.visits_controller import api as visit_ns
from app.main.controllers.products_controller import api as product_ns

blueprint = Blueprint('api', __name__)

api = Api(
	blueprint,
	title='STORELIFT API',
	version='0.1.0',
	description='Api for store actions'
)

api.add_namespace(user_ns, path='/users')
api.add_namespace(visit_ns, path='/visits')
api.add_namespace(product_ns, path='/products')
