from packjoy.app import m

product = m.Product

# A freeeeaking helper 
# to get an index, 
# or handle exception
def get_list_index(list, di, default):
	try:
		return list[di]
	except IndexError:
		return default


# Gives us back a product dictionary 
# or None
# based on slug
def get_prods_by_slug(slug):
	if slug is None:
		return product.list()
	data = m.get('products/?slug={}'.format(slug))
	return get_list_index(data, 0, None)