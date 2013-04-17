from itertools import combinations, islice

def prime_pairs(primes):
	for a, b in combinations(primes, 2):
		concat1 = int(str(a) + str(b))
		concat2 = int(str(b) + str(a))
		#if concat1 > limit or concat2 > limit:
		#	pass#print 'Sieve too small!'
		if not isPrime(concat1) or not isPrime(concat2):
			return False
	return True

from timeit import Timer
t = None
def test_prime_pairs(times, combi_size):
	global t
	t = Timer('[prime_pairs(combi,%d) for combi in combinations(xrange(100))]' % combi_size, "from __main__ import prime_pairs; from itertools import combinations")
	print t.timeit(1)

if __name__ == '__main__':
	test_prime_pairs(1,2)