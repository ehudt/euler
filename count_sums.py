# problem 76

from memoize import memoize

# for each series length, allow the first number to be no less than n / len(series) 
# and no more than n + 1 - len(series).
# length of series can be between 2 and n
@memoize
def summations(n, length):
	if length == 1: return 1
	sums = 0
	for first in xrange((n-1)/length + 1, n - length + 2):
		sums += summations(n - first, length - 1)
	return sums

def count_summations(n):
	if n <= 1: return 0
	return sum(summations(n, length) for length in xrange(2, n + 1))

if __name__ == '__main__':
	print count_summations(10)