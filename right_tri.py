# problem 75 - correct solution

from collections import defaultdict, deque

from streams import interleave

def coprime_pairs(limit):
	queue = deque()
	queue.append((2,1))
	def helper():
		while queue:
			m, n = queue.popleft()
			if 2 * m * (m + n) <= limit:
				queue.append((2*m-n, m))
				queue.append((2*m+n, m))
				queue.append((m+2*n, n))
				yield (m, n)
	return helper()

def main():
	limit = 1500000
	all_pairs = coprime_pairs(limit)
	counter = defaultdict(lambda : 0)
	for m, n in all_pairs:
		k = 1
		while True:
			a = k*(m*m - n*n)
			b = k*(2*m*n)
			c = k*(m*m + n*n)
			if a + b + c > limit: break
			counter[a+b+c] += 1
			k += 1
	total = 0
	for i in xrange(limit + 1):
		if counter[i] == 1:
			total += 1
	print total

if __name__ == '__main__':
	main()

	