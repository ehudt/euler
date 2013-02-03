fact = lambda n: 1 if n is 0 else n*fact(n-1)
f = {fact(n) for n in xrange(1,10)}

accum = 0
for i in xrange(10, 10000000):
	if i == sum(map(fact, map(int, [c for c in str(i)]))):
		print i
		accum += i

print accum