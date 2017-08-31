import uuid 
from packjoy.app import db, pp

# This needs to be moved somewhere else
class Email(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True)
    token = db.Column(db.String(20), unique=True)

    def __init__(self, email):
        self.email = email
        self.token = uuid.uuid4().hex[:8].upper()

    def __repr__(self):
        return '<Subscriber %r>' % self.email

class Product(object):
	def __init__(self, data):
		# pp.pprint(data)
		self.created_at = data['created_at']
		self.description = data['description']
		self.id = data['id']
		self.images = [image['url']['https'] for image in data['images']]
		self.price = data['price']['value']
		self.slug = data['slug']
		self.stock_level = data['stock_level']
		self.title = data['title']
		self.brand = {
			'title': data['brand']['data']['title'],
			'slug': data['brand']['data']['slug'],
		}
		self.category = [data['category']['data'][cat_id] for cat_id in data['category']['data']]

	def get_stock_status(self):
		if int(self.stock_level) <= 5:
			return '{} pieces left'.format(self.stock_level)
		elif int(self.stock_level) > 5 and int(self.stock_level) <=15:
			return 'Low Stock'
		else: 
			return 'In stock'
		