from .. import db

class Cart(db.Model):
	""" Cart Model for storing cart-related details """
	__tablename__ = 'cart'

	id					= db.Column(db.Integer, primary_key=True, autoincrement=True)
	total				= db.Column(db.Integer, default=0)
	visit_id		= db.Column(db.Integer, db.ForeignKey('visit.id'), nullable=False, unique=True)
	checked_out	= db.Column(db.Boolean, default=False)
	products		= db.relationship('Product', backref='cart')

	@property
	def __repr__(self):
		return "<Cart: '{id}', total: {total}, checked_out: {checked_out}, visit_id: {visit_id}>".format(id=self.id, total=self.total, visit_id=self.visit_id, checked_out=self.checked_out)

