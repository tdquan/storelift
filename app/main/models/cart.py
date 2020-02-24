from .. import db

class Cart(db.Model):
	""" Cart Model for storing cart-related details """
	__tablename__ = 'cart'

	id					= db.Column(db.Integer, primary_key=True, autoincrement=True)
	public_id 	= db.Column(db.String(100), unique=True)
	total				= db.Column(db.Integer, default=0)
	visit_id		= db.Column(db.Integer, db.ForeignKey('visit.id'), nullable=False, unique=True)
	checked_out	= db.Column(db.Boolean, default=False)
	products		= db.relationship('Product', backref='cart', lazy='dynamic')


