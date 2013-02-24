# problem 71

from fractions import Fraction
limit = 800
s = set()
for d in xrange(2, limit + 1):
	for n in xrange(1, d):
		s.add(Fraction(n,d))

l = sorted(list(s))
print l[l.index(Fraction(3,7)) - 1]
print l