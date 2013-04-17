def phi(max_n):
	phis = [n for n in xrange(max_n + 1)]
	for i in xrange(2, max_n + 1):
		if phis[i] == i:
			for j in xrange(i, max_n + 1, i):
				phis[j] = (phis[j] / i) * (i - 1)
	return phis

max_n = 12000
p = phi(max_n)
print p
d = {2}
for i in xrange(3, max_n + 1):
	n = i
	if n % 2 == 0: n /= 2
	if n % 3 == 0: n /= 3
	d.add(n)
print sum(p)
print sum(p[i] for i in d)
print p[131]


def gcd(a, b):
    """Return greatest common divisor using Euclid's Algorithm."""
    while b:      
        a, b = b, a % b
    return a