from datetime import datetime

from .. import db

class Visit(db.Model):
	""" Visit Model for storing visit related details """
	__tablename__ = 'visit'

	id 					= db.Column(db.Integer, primary_key=True, autoincrement=True)
	public_id 	= db.Column(db.String(100), unique=True)
	time_enter	= db.Column(db.DateTime, nullable=False, default=datetime.utcnow())
	time_exit		= db.Column(db.DateTime)
	user_id			= db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
	cart				= db.relationship('Cart', backref='visit', uselist=False)
	products		= db.relationship('Product', secondary='cart', viewonly=True, lazy='dynamic')
