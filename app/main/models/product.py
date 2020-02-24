from .. import db

class Product(db.Model):
	""" Product Model for storing product-related details """
	__tablename__ = 'product'

	id				= db.Column(db.Integer, primary_key=True, autoincrement=True)
	name			= db.Column(db.String(500), nullable=False)
	price			= db.Column(db.Integer, nullable=False, default=0)
	cart_id		= db.Column(db.Integer, db.ForeignKey('cart.id'))
	public_id	= db.Column(db.String(100), unique=True)
	available	= db.Column(db.Boolean, default=True)
