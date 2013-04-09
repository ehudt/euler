# problem 187

limit = 10**8
factors = [0]*limit

factors[1] = 1

def part(n, p):
	count = 0
	while n % p == 0:
		n /= p
		count += 1
	return count

for i in xrange(2, limit):
	if factors[i] == 0:
		for j in xrange(i, limit, i):
			factors[j] += part(j, i)

print len([x for x in factors if x == 2])
