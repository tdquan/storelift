import uuid
from datetime import datetime

from app.main import db
from app.main.models.visit import Visit
from .shared import save

class VisitService:
	""" Visit-related operations """

	def create_visit(self, data):
		visit = Visit(
			public_id = str(uuid.uuid4()),
			time_enter = datetime.utcnow(),
			user_id = data['user_id']
		)

		if save(visit):
			return visit
		else:
			return None

	def end_visit(self, public_id):
		visit = self.find_visit(public_id)
		visit.time_exit = datetime.utcnow()
		db.session.commit()

	def find_visit(self, public_id):
		return Visit.query.filter_by(public_id=public_id).first()

	def all_visits():
		return Visit.query.all()
