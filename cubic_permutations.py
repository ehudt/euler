# problem 62

from collections import Counter

limit = 10000

cubes = [x*x*x for x in xrange(limit)]

perms = {}

def main():
	for cube in cubes:
		counter = Counter(str(cube))
		perms[cube] = [x for x in cubes if cube in perms.get(x, []) or Counter(str(x)) == counter]
		if len(perms[cube]) == 5:
			print cube

if __name__ == '__main__':
	main()

