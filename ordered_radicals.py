# problem 124

limit = 100000

radicals = [1] * (limit + 1)

for i in xrange(2, limit + 1):
	if radicals[i] == 1:
		for j in xrange(i, limit + 1, i):
			radicals[j] *= i

order = sorted([(radicals[i], i) for i in xrange(limit + 1)])

print order[10000][1]