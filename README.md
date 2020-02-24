# Storelift

### Start the project:

- Simply navigate to the root folder and run
```shell
python3 -m venv venv
or
python -m venv venv # if python3 is already active
```
- Then:
```shell
. venv/bin/activate
pip install -r /requirements.txt
```

- Finally start the server:
```shell
python manage.py run
```

Swagger API interface will be then available for testing

### Run the script:

- With the server running, open another shell, navigate to the project directory and run:
```shell
python script.py
```

### Things can be added:
- Issue expirable token for every start of a visit. Only allow 1 active visit at a time by expiring existing token when a new one is issued.
- Token can be used for every api call to provide security.
- Other models to deal with payment/transaction
- Availability of product is False when the product is added to cart
- Check for product's availability when adding to the cart and only list available products
- Tests
