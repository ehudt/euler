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
		#self.l = [k for k in xrange(self.size) if self.isPrime(k)]
	def isPrime(self, n):
		return self.d[n] if 0 <= n < self.size else False
	def __iter__(self):
		return (k for k in xrange(self.size) if self.isPrime(k))
	def __len__(self):
		return len([k for k in xrange(self.size) if self.isPrime(k)])
	def prime_list(self):
		return [k for k in xrange(self.size) if self.isPrime(k)]
