from packjoy.app import m, pp
from packjoy.models import Product, Brand
from moltin.exception import RequestError


product = m.Product

# A freeeeaking helper 
# to get an index of a list, 
# or handle exception
def get_list_index(list, di, default):
	try:
		return list[di]
	except IndexError:
		return default


# Gives us back a product dictionary
# (Product Model instances)
# or None
# based on slug
def get_prods_by_slug(slug):
	if slug is None:
		prod_list = product.list()
		# Should ADD TO MODEL ONE BY ONE
		# USE dict comprehension maybe
		data = [Product(prod_list[i]) for i in range(0,4)]
		return data
	try:
		data = m.get('products/?slug={}'.format(slug))
	except RequestError as e:
		data = e
	prod = get_list_index(data, 0, None)
	if prod:
		return Product(prod)
	else: 
		return None

# Gives back a brand object (model)
# or None
def get_brand_by_slug(brand_slug):
	# Test this
	data = product.list()
	data = [prod for prod in data if prod['brand']['data']['slug'] == brand_slug]
	if len(data) == 0 or data is None:
		return None
	prod_list = [Product(prod) for prod in data]
	brand = Brand(products=prod_list)
	return brand