# problem 100

limit = 20000

def solve(m, l):
	return 2*m*(m-1) == (10**12 + l) * (10**12 - 1 + l)

for m in xrange(2, limit):
	for l in xrange(limit):
		if solve(m, l):
			print m, l