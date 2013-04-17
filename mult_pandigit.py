def vecProduct(n, tup):
	s = []
	for i in tup:
		s.append(str(n*i))
	return ''.join(s)

def tuplesFor(n):
	nlen = len(str(n))
	to = max(2, 9 / nlen + 1)
	fr = max(2, to / 2 - 1)
	for i in xrange(fr, to + 1):
		yield (j for j in range(1,i + 1))

def allDigits(s):
	if len(s) != 9:
		return False
	for c in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
		if s.count(c) != 1:
			return False
	return True

def main():
	max_prod = 0
	for i in xrange(10000):
		for tup in tuplesFor(i):
			sprod = vecProduct(i, tup)
			prod = int(sprod)
			if allDigits(sprod) and prod > max_prod:
				max_prod = prod
	print max_prod

if __name__ == '__main__':
	main()