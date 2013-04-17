
def memoize(func):
	def wrapper(*args):
		if args in wrapper.d:
			return wrapper.d[args]
		ret_val = func(*args)
		wrapper.d[args] = ret_val
		return ret_val
	wrapper.d = {}
	return wrapper
