from collections import defaultdict

class Sieve(object):
	"""Generate a sieve of selected size"""
	def __init__(self, size):
		super(Sieve, self).__init__()
		if size <= 0:
			raise ValueError("Sieve size must be at least 1")
		self.size = size
		d = defaultdict(lambda : True)
		d[0] = d[1] = False
		for i in xrange(2, size):
			if d[i] is False:
				continue
			for j in xrange(i*i, size, i):
				d[j] = False
		self.d = d
		self.l = [k for k in self.d if self.d[k] is True]
	def isPrime(self, n):
		return self.d[n] if 0 <= n < self.size else False
	def __iter__(self):
		for k in self.l:
			yield k

sieve = Sieve(100000)



def findPrimeLimit(a, b):
	n = 0
	while sieve.isPrime(n*n + a*n + b) and n < abs(b):
		n += 1
	return n - 1

def allPolys():
	for b in sieve:
		if b >= 1000:
			break
		for a in xrange(1000):
			if not sieve.isPrime(1 + a + b):
				continue
			yield a, b
			yield -a, b
			yield a, -b
			yield -a, -b

def main():
	max_prod = 0
	max_prime = 0
	max_a = 0
	max_b = 0
	for a, b in allPolys():
		limit = findPrimeLimit(a, b)
		#if limit > 1000:
	#		print a, b, limit
		if limit > max_prime:
			max_prod = a*b
			max_prime = limit
			max_a = a
			max_b = b
	print max_prime, max_prod
	print max_a, max_b

if __name__ == '__main__':
	main()