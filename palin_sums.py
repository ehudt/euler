# problem 125
from math import sqrt

limit = 10000

def make_sum_consecutive_squares(limit):
	squares = [x*x for x in xrange(int(sqrt(limit)) + 1)]
	memo = {}
	def sum_consecutive_squares(n):
		for biggest in xrange(int(n**.5) + 1, 1, -1):
			for series in xrange(2, biggest):
				if (biggest-series, biggest) not in memo:
					memo[(biggest-series, biggest)] = sum(squares[biggest-series:biggest])
				series_sum = memo[(biggest-series, biggest)]
				if series_sum > n:
					break
				if series_sum == n:
					return True
		return False
	return sum_consecutive_squares

def is_palindrome(n):
	str_n = str(n)
	return str_n == str_n[::-1]

def check(n):
	return is_palindrome(n) and sum_consecutive_squares(n)

sum_consecutive_squares = make_sum_consecutive_squares(limit)
print sum(x for x in xrange(limit) if check(x))