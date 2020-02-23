from .. import db

class User(db.Model):
	""" User Model for storing user related details """
	__tablename__ = 'user'

	id 				= db.Column(db.Integer, primary_key=True, autoincrement=True)
	public_id = db.Column(db.String(100), unique=True)
	visits		= db.relationship('Visit', backref='visitor')

	@property
	def __repr__(self):
		return "<User '{}'>".format(self.public_id)
