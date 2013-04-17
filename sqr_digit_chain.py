# problem 92

memo = {}

def next(n):
	if n in memo:
		return memo[n]
	output = 0
	while n > 0:
		output += (n%10)**2
		n /= 10
	memo[n] = output
	return output

def main():
	count = 0
	for i in xrange(2,10000000):
		n = i
		while n != 1 and n != 89:
			n = next(n)
		memo[i] = n
		if n == 89:
			count += 1
	print count

if __name__ == '__main__':
	main()
