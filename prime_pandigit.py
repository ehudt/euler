from math import sqrt

def all_permutations(l):
	if len(l) == 0:
		yield ''
	for s in l:
		newl = list(l)
		newl.pop(newl.index(s))
		for t in all_permutations(newl):
			yield s + t

def is_prime(n):
	for i in xrange(2, int(sqrt(n)) + 1):
		if n % i == 0:
			return False
	return True

def main():
	max_pan_prime = 0
	for i in xrange(8, 1, -1):
		l = [str(x) for x in xrange(1, i + 1)][::-1]
		for p in all_permutations(l):
			n = int(p)
			if is_prime(n):
				print n
				return

if __name__ == '__main__':
	main()
