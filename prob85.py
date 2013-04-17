def combi(n, m):
	return n*(n-1)*m*(m-1)/4

min_delta = 2000000
target = 2000000
pair = (1,1)
for n in xrange(1,8000):
	for m in xrange(n, 8000):
		delta = abs(combi(n+1,m+1) - target)
		if delta < min_delta:
			min_delta = delta
			pair = (n, m)
print pair
print min_delta
