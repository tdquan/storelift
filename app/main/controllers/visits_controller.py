from flask import request
from flask_restplus import Resource

from app.main.utils.dto import VisitDTO
from app.main.services.visit_service import VisitService

api = VisitDTO.api
_visit = VisitDTO.visit
service = VisitService()

@api.route('/', strict_slashes=False)
class Visits(Resource):
	@api.doc('List all visits')
	@api.marshal_list_with(_visit, envelope='data')
	def get(self):
		""" List all visits """
		return service.all_visits()

	@api.doc('When user enters the store')
	@api.response(201, 'User entered')
	@api.response(409, 'User failed to enter')
	@api.expect(_visit, validate=True)
	def post(self):
		""" Create a new visit """
		data = request.json
		return service.create_visit(data)
