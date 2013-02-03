# problem 61

def all_ints():
	n = 1
	while True:
		yield n
		n += 1

def triangle():
	return (n * (n + 1) / 2 for n in all_ints())

def square():
	return (n * n for n in all_ints())

def pentagonal():
	return (n * (3 * n - 1) / 2 for n in all_ints())

def hexagonal():
	return (n * (2 * n - 1) for n in all_ints())

def heptagonal():
	return (n * (5 * n -3) / 2 for n in all_ints())

def octagonal():
	return (n * (3 * n - 2) for n in all_ints())

def is_cyclic(tup):
	for a, b in zip(tup, tup[1:] + tup[:1]):
		if a % 100 != b / 100:
			return False
	return True

def iter4digits(iter):
	for n in iter:
		if n > 9999:
			break
		if n > 999:
			yield n

from itertools import product, combinations

triangles = {x for x in iter4digits(triangle())}
squares = {x for x in iter4digits(square())}
pentagonals = {x for x in iter4digits(pentagonal())}
hexagonals = {x for x in iter4digits(hexagonal())}
heptagonals = {x for x in iter4digits(heptagonal())}
octagonals = {x for x in iter4digits(octagonal())}
alls = triangles.union(squares).union(pentagonals).union(hexagonals).union(heptagonals).union(octagonals)


def main():
	print 'Starting search...'
	for tup in product(alls, repeat=6):
		if is_cyclic(tup):
			print tup

if __name__ == '__main__':
	main()