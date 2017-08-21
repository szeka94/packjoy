from packjoy.app import m

product = m.Product

def get_prods_by_slug(slug):
	print(slug)
	if slug is None:
		return product.list()
	return product.find_by({ 'slug': slug })[0]