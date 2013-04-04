# problem 75 - bad solution

from collections import defaultdict

def interleave(gen1, gen2):
	try:
		yield gen1.next()
	except StopIteration:
		for x in gen2:
			yield x
	for x in interleave(gen2, gen1):
		yield x

def coprime_pairs():
	def helper(m, n):
		yield (m, n)
		for x in interleave(helper(2*m - n , m), \
						  interleave(helper(2*m + n, m), helper(m + 2*n, n))):
			yield x
	return helper(2, 1)

def main():
	limit = 50
	all_pairs = coprime_pairs()
	counter = defaultdict(lambda : 0)
	for m, n in all_pairs:
		k = 1
		while True:
			a = k*(m*m - n*n)
			b = k*(2*m*n)
			c = k*(m*m + n*n)
			if a+b+c > limit: break
			counter[a+b+c] += 1
			k += 1
		if m*m + n*n >= limit / 2: break
	total = 0
	for i in xrange(limit + 1):
		if counter[i] == 1:
			total += 1
	print total

if __name__ == '__main__':
	main()

	