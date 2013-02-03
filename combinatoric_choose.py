from itertools import izip

def limit_ncr(n, r, limit=1000000):
	if r <= n/2:
		r = n - r
	res = 1
	for enum, denom in izip(xrange(n - r + 1, n + 1), xrange(1, r + 1)):
		res *= float(enum) / denom
		if res > limit:
			break
	return int(round(res))

def main():
	counter = 0
	for n in xrange(1, 101):
		for r in xrange(0, n + 1):
			if limit_ncr(n, r) > 1000000:
				counter += 1
	print counter

if __name__ == '__main__':
	main()