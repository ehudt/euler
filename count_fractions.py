# problem 72
# a sieving method for phi(n) - euler's totient
limit = 1000000
phi = range(limit + 1)
count = 0
for i in xrange(2, limit + 1):
	if phi[i] == i:
		for j in xrange(i, limit + 1, i):
			phi[j] = phi[j] / i * (i - 1)
	count += phi[i]

print count