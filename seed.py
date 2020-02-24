import uuid
from random import randint

from manage import app
from app.main import db
from app.main.services.product_service import ProductService
from app.main.services.user_service import UserService
from app.main.models.user import User
from app.main.models.visit import Visit
from app.main.models.cart import Cart
from app.main.models.product import Product

app.app_context().push()

# user names
users = (
	"Alexane Collins",
	"Giovani Romaguera",
	"Jailyn Pagac",
	"Sigmund Legros",
	"Ken Wehner",
	"Josh Ryan",
	"Zackary Bauch"
)

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

product_service = ProductService()
user_service = UserService()

# Create users from names
for name in users:
	email = '_'.join(name.lower().split(' '))
	user = { 'email': "{email}@email.com".format(email=email) }
	user_service.create_user(user)

# Add random products
for name in products:
	product = { 'name': name, 'price': randint(300, 1000) }
	for _ in range(randint(1, 20)):
		product_service.create_product(product)
