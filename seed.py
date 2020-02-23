import uuid
from random import randint

from manage import app
from app.main import db
from app.main.services.product_service import ProductService
# from app.main.services.user_service import UserService
from app.main.models.user import User
from app.main.models.visit import Visit
from app.main.models.cart import Cart
from app.main.models.product import Product

app.app_context().push()

# List of product names for seeding
products = (
	"Addictive Sweet Potato Burritos",
	"Asian Noodle Salad",
	"Beef with Snow Peas",
	"Blueberry Zucchini Bread",
	"Cheesy Bread",
	"Creamy Avocado Yogurt Dip",
	"Creamy Rice Pudding",
	"French Onion Soup Stuffed Mushrooms",
	"Fresh Mint Chip Frozen Yogurt",
	"Frozen Hot Chocolate"
)

# Clearing all data in the db for fresh seeding
for table in reversed(db.metadata.sorted_tables):
	print("Clearing table {table_name}...".format(table_name=table))
	db.session.execute(table.delete())

db.session.commit()

# Add random products
for name in products:
	service = ProductService()
	data = { 'name': name, 'price': randint(300, 1000) }
	for _ in range(randint(1, 20)):
		service.create_product(data)
