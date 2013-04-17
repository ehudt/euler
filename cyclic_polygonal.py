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
d = {3:triangles, 4:squares, 5:pentagonals, 6:hexagonals, 7:heptagonals, 8:octagonals}
groups = [triangles, squares, pentagonals, hexagonals, heptagonals, octagonals]
alls = triangles.union(squares).union(pentagonals).union(hexagonals).union(heptagonals).union(octagonals)
from collections import defaultdict
prefixes = defaultdict(lambda : [])

for num in alls:
	prefixes.setdefault(int(num)/100, []).append(num)

def check_representors(i):
	grp = set(range(3,9))
	nums = set(i)
	count = 1
	for num in nums:
		if sum(1 for group in grp if num in d[group]) == 0:
			return False
	
	while len(nums) > 0 and count <= 6:
		to_remove = set()
		for num in nums:
			ll = [group for group in grp if num in d[group]]
			if len(ll) == count:
				#print num, ll,
				for group in ll:
					grp.remove(group)
				to_remove.add(num)
		for num in to_remove:
			nums.remove(num)
		count += 1
	#print ''
	return len(grp) == 0 and len(nums) == 0

def main():
	i = [0, 0, 0, 0, 0, 0]
	for i[0] in alls:
		for i[1] in prefixes[i[0] % 100]:
			for i[2] in prefixes[i[1] % 100]:
				for i[3] in prefixes[i[2] % 100]:
					for i[4] in prefixes[i[3] % 100]:
						for i[5] in prefixes[i[4] % 100]:
							if i[5] % 100 == i[0] / 100 and check_representors(i):
								print i
								print sum(i)

if __name__ == '__main__':
	main()