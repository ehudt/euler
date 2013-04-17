# problem 60

from sieve import Sieve
from itertools import combinations, islice
from math import sqrt

limit = 10000
sieve = Sieve(limit)
big_sieve = Sieve(1000000)

def prime_combinations(primes, size, required_sum):
	#if required_sum < size * 2:
	#	pass
	if required_sum == 0 and size != 0:
		pass
	elif size == 0:
		if required_sum == 0:
			yield []
		else:
			pass
	else:
		for p in primes:
			if p > (required_sum - (size - 1) * 2):
				break
			for combi in prime_combinations(primes, size - 1, required_sum - p):
				yield combi + [p]

def minimal_combinations(l, size):
	if size == 1:
		for x in l:
			yield (x,)
	else:
		for i, largest in enumerate(l):
			if i < size - 1:
				continue
			for combi in minimal_combinations(l[:i], size - 1):
				yield combi + (largest,)

prime_cache = {2}

def isPrime(p):
	global prime_cache
	if p in prime_cache:
		return True
	elif p <= 1:
		return False
	for i in xrange(2, int(sqrt(p)) + 1):
		if p % i == 0:
			return False
	prime_cache.add(p)
	return True

xxx = {}

def prime_pairs(primes):
	global xxx
	for a, b in combinations(primes, 2):
		'''if b in xxx.get(a, set()) and a in xxx.get(b, set()):
			continue'''
		sa = str(a)
		sb = str(b)
		sasb = sa+sb
		concat1 = int(sasb)
		concat2 = int(sb + sa)
		#if concat1 > limit or concat2 > limit:
		#	pass#print 'Sieve too small!'
		if len(sasb) <= 5:
			if not big_sieve.isPrime(concat1) or not big_sieve.isPrime(concat2):
				return False
			'''else:
				xxx.setdefault(a, set()).add(b)
				xxx.setdefault(b, set()).add(a)'''
		else:
			if not isPrime(concat1) or not isPrime(concat2):
				return False
			'''else:
				xxx.setdefault(a, set()).add(b)
				xxx.setdefault(b, set()).add(a)'''
	return True
'''
dd = {}
prime_set = {}
def main():
	d = {}
	global prime_set
	prime_set = {x : set() for x in sieve.prime_list()}
	#for primes in combinations(prime_set, group_size):
	for size in xrange(2*limit):
		for primes in prime_combinations(sieve.prime_list(), 2, size):
			if prime_pairs(primes):
				prime_set[primes[0]].add(primes[1])
				prime_set[primes[1]].add(primes[0])
				print sum(primes)
				print primes
	for prime in prime_set.keys():
		for item in list(prime_set[prime]):
			if len(prime_set.get(item,[])) < 5:
				prime_set[prime].remove(item)
		if len(prime_set[prime]) < 5:
			del(prime_set[prime])
	print prime_set
	for size in xrange(5*limit):
		for primes in prime_combinations(prime_set.keys(), 5, size):
			if prime_pairs(primes):
				print sum(primes)
				print primes
'''


'''def main2():
	l = sieve.prime_list()
	for set_limit in xrange(4, limit):
		print set_limit
		largest = l[set_limit - 1]
		for primes in combinations(l[:set_limit], 4):
			if largest not in primes:
				continue
			if prime_pairs(primes):
				print sum(primes)
				print primes
'''
dd = {}
prime_set = {}
def main():
	d = {}
	global prime_set
	prime_set = {x : set() for x in sieve.prime_list()}
	for group_size in [2, 5]:
		for primes in combinations(prime_set, group_size):
			if prime_pairs(primes):
				prime_set[primes[0]].add(primes[1])
				prime_set[primes[1]].add(primes[0])
				print sum(primes)
				print primes
		for prime in prime_set.keys():
			for item in list(prime_set[prime]):
				if len(prime_set.get(item,[])) < 5:
					prime_set[prime].remove(item)
			if len(prime_set[prime]) < 5:
				del(prime_set[prime])
	print prime_set




'''
def main():
	for size in xrange(4*limit):
		for primes in prime_combinations(sieve.prime_list(), 4, size):
			if prime_pairs(primes):
				print sum(primes)
				print primes
	'''


if __name__ == '__main__':
	main()

