import sys

def pentagonal(n):
	return n*(3*n-1)/2

limit = 10000

pent = {pentagonal(n) for n in xrange(1, limit)}


min_d = sys.maxint

for i in xrange(1, limit):
	for j in xrange(i + 1, limit):
		if pentagonal(i) + pentagonal(j) in pent and abs(pentagonal(i) - pentagonal(j)) in pent:
			print abs(pentagonal(i) - pentagonal(j))
			if abs(pentagonal(i) - pentagonal(j)) < min_d:
				min_d = abs(pentagonal(i) - pentagonal(j))
print min_d