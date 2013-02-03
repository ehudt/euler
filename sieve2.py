from itertools import ifilter

def all_ints(initial=1):
	i = initial
	while True:
		yield i
		i += 1

def sieve():
	ints = all_ints(2)
	while True:
		p = ints.next()
		yield p
		ints = ifilter(lambda x: x % p != 0, ints)