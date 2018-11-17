
def get_item():
	rv = cache.get('item')

	if rv is None:
		rv = calculate_value()
		cache.set('item', rv, timeout = 5*60)

	return rv
