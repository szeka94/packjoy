from packjoy.app import m

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
# or None
# based on slug
def get_prods_by_slug(slug):
	if slug is None:
		return product.list()
	try:
		data = m.get('products/?slug={}'.format(slug))
	except RequestError as e:
		data = e
	print(data)
	return get_list_index(data, 0, None)