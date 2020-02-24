import json
from requests import post, put, get

from manage import app
from app.main.models.user import User
from app.main.models.product import Product

app.app_context().push()

customer_a = User.query.all()[0]
customer_b = User.query.all()[-1]
product_1 = Product.query.all()[0]
product_2 = Product.query.all()[-1]
product_3 = Product.query.all()[33]
product_4 = Product.query.all()[43]
product_5 = Product.query.all()[53]

headers = {"content-type": "application/json"}

print('Customer A\'s journey:')
# - Customer A enters the store
a_pid = customer_a.public_id
response = put('http://localhost:5000/users/{customer_a_public_id}/enter'.format(customer_a_public_id=a_pid))
print(response.text)
# - Customer A takes the product 1
data = json.dumps({ "public_id": product_1.public_id })
response = put('http://localhost:5000/users/{customer_a_public_id}/add_to_cart'.format(customer_a_public_id=a_pid), data=data, headers=headers)
print(response.text)
# - Customer A takes the product 2
data = json.dumps({ "public_id": product_2.public_id })
response = put('http://localhost:5000/users/{customer_a_public_id}/add_to_cart'.format(customer_a_public_id=a_pid), data=data, headers=headers)
print(response.text)
# - Customer A exits the store
response = put('http://localhost:5000/users/{customer_a_public_id}/check_out'.format(customer_a_public_id=a_pid))
print(response.text)
print('-----')
visit = customer_a.visits[-1]
print('Visitor {public_id} bought these items:'.format(public_id=visit.public_id))
for product in visit.cart.products:
	print(product.name)

print()
print()

print('Customer B\'s journey:')
# - Customer B enters the store
b_pid = customer_b.public_id
response = put('http://localhost:5000/users/{customer_b_public_id}/enter'.format(customer_b_public_id=b_pid))
print(response.text)
# - Customer B takes the product 3
data = json.dumps({ "public_id": product_3.public_id })
response = put('http://localhost:5000/users/{customer_b_public_id}/add_to_cart'.format(customer_b_public_id=b_pid), data=data, headers=headers)
print(response.text)
# - Customer B takes the product 4
data = json.dumps({ "public_id": product_4.public_id })
response = put('http://localhost:5000/users/{customer_b_public_id}/add_to_cart'.format(customer_b_public_id=b_pid), data=data, headers=headers)
print(response.text)
# - Customer B takes the product 5
data = json.dumps({ "public_id": product_5.public_id })
response = put('http://localhost:5000/users/{customer_b_public_id}/add_to_cart'.format(customer_b_public_id=b_pid), data=data, headers=headers)
print(response.text)
# - Customer B put back product 4
data = json.dumps({ "public_id": product_4.public_id })
response = put('http://localhost:5000/users/{customer_b_public_id}/remove_from_cart'.format(customer_b_public_id=b_pid), data=data, headers=headers)
print(response.text)
# - Customer B exits the store
response = put('http://localhost:5000/users/{customer_b_public_id}/check_out'.format(customer_b_public_id=b_pid))
print(response.text)
print('-----')
visit = customer_b.visits[-1]
print('Visitor {public_id} bought these items:'.format(public_id=visit.public_id))
for product in visit.cart.products:
	print(product.name)
