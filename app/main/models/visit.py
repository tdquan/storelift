from datetime import datetime

from .. import db

class Visit(db.Model):
	""" Visit Model for storing visit related details """
	__tablename__ = 'visit'

	id 					= db.Column(db.Integer, primary_key=True, autoincrement=True)
	time_enter	= db.Column(db.DateTime, nullable=False, default=datetime.utcnow())
	time_exit		= db.Column(db.DateTime)
	user_id			= db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
	cart				= db.relationship('Cart', backref='visit', uselist=False)
	products		= db.relationship('Product', secondary='cart', viewonly=True)

	@property
	def __repr__(self):
		return "<Visit: '{id}', time_enter: {time_enter}, user_id: {cart_id}>".format(id=self.id, time_enter=self.time_enter, user_id=self.user_id)
