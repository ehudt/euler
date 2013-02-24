# problem 76

memo = {0 : 1, 1 : 1, }

def count_sums(n,lim):
	#if n in memo: 
	#	return memo[n]
	if n < 2: 
		return 1
	count = 0
	for i in xrange(n - 1, 0, -1):
		count += count_sums(i, i)
	return count

print count_sums(5, 4)
