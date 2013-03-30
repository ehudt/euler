# problem 71

from fractions import Fraction

def min_strong(l):
	current = l[0]
	min_i = 0
	weak = True
	for i in xrange(len(l)):
		item = l[i]
		if item < current:
			current = item
			min_i = i
			weak = False
	return min_i, weak


l = [0]*11
finished = False
i, _ = min_strong(l)
while not finished:
	l[i] += i+1
	i, finished = min_strong(l)

print l[0]

