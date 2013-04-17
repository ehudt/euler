# problem 145

import operator

def reverse_num(n):
	return int(str(n)[::-1])

#def odd_digits(n):
#	return reduce(operator.and_, map(lambda x: x % 2 == 1, map(int, list(str(n)))), True)

def odd_digits(n):
	odd = True
	while n:
		odd, n = odd & ((n%10)%2==1), n/10
	return odd

def main():
	limit = 1000000000
	print sum(1 for i in xrange(1, limit) if odd_digits(i + reverse_num(i)) and i%10 != 0)

if __name__ == '__main__':
	main()
