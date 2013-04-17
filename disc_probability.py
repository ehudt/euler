# problem 100

# n = 21, m = 15 : m/n * (m-1)/(n-1) = 1/2


#from numpy import allclose
from fractions import Fraction

def prob(n, m):
	return Fraction(m*(m-1), n*(n-1))

for n in xrange(20, 200):
	for m in xrange(2, n):
		if prob(n, m) == Fraction(1,2):
			print n, m