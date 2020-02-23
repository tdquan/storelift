from .. import db

class Product(db.Model):
	""" Product Model for storing product-related details """
	__tablename__ = 'product'

	id				= db.Column(db.Integer, primary_key=True, autoincrement=True)
	name			= db.Column(db.String(500), nullable=False)
	price			= db.Column(db.Integer, nullable=False, default=0)
	cart_id		= db.Column(db.Integer, db.ForeignKey('cart.id'))
	public_id	= db.Column(db.String(100), unique=True)

	@property
	def __repr__(self):
		return "<Product: '{public_id}', name: '{name}', price: {price}, cart_id: {cart_id}>".format(public_id=self.public_id, name=self.name, cart_id=self.cart_id, price=self.price)
