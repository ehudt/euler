
# problem 87

from sieve import Sieve

d = set()

for i in Sieve(7100):
	for j in Sieve(400):
		for k in Sieve(100):
			res = i*i + j*j*j + k*k*k*k
			if res < 50000000:
				d.add(res)
print len(d)
