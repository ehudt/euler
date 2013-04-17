from math import sqrt
#from sieve_ext import eratosthenes
#from itertools import islice

def diagonals():
	accum = 1
	current = 1
	dim = 1
	yield current
	while True:
		dim += 2
		current += 2
		for i in xrange(4):
			yield current
			accum += current
			current += dim - 1

def layer(index):
	return (index - 1)/4 + 1

def side_len(index):
	return layer(index)*2 + 1

def isPrime(p):
	if p <= 1:
		return False
	for i in xrange(2, int(sqrt(p)) + 1):
		if p % i == 0:
			return False
	return True

def main():
	index = 0
	primes = 0
	for i in diagonals():
		if isPrime(i):
			primes += 1
		if index > 0 and index % 4 == 0 and (primes/float(index + 1) < 0.1):
			print side_len(index), primes/float(index + 1), i
			return
		index += 1

if __name__ == '__main__':
	main()

