from packjoy.app import m, pp
from packjoy.models import Product

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
		pp.pprint(p for p in prod_list)
		return prod_list
	try:
		data = m.get('products/?slug={}'.format(slug))
	except RequestError as e:
		data = e
	prod = get_list_index(data, 0, None)
	if prod:
		return Product(prod)
	else: 
		return None