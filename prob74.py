#problem 74
fact = lambda n: 1 if n <= 1 else n * fact(n-1)
fact_d = {n:fact(n) for n in xrange(10)}

def digit_fact(n):
	return sum(map(fact, map(int, list(str(n)))))

def chain(n):
	d = set()
	count = 0
	while n not in d:
		count += 1
		d.add(n)
		n = digit_fact(n)
	return count

chain_count = 0
limit = 1000000
for i in xrange(1, limit):
	if chain(i) == 60:
		chain_count += 1

print chain_count 