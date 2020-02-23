from app.main import db

def save(data):
	committed = True
	db.session.add(data)
	try:
		db.session.commit()
	except Exception as e:
		print(e)
		db.session.rollback()
		db.session.flush()
		committed = False

	return committed
