# Pandigital Fibonacci ends
# Problem 104

from collections import Counter
from itertools import izip

def check(l):
	c = Counter(l)
	if 0 in c or len(c) != 9:
		return False
	for i in c:
		if c[i] != 1:
			return False
	return True

def pandigital_last(n):
	l = []
	for i in xrange(9):
		l.append(n % 10)
		n /= 10
	return check(l)
	
def pandigital_first(n):
	while n >= 1000000000:
		n /= 10
	return pandigital_last(n)

def fibonacci(f=lambda x:x):
	fn_1, fn_2 = 1, 1
	yield 1
	while True:
		yield fn_1
		fn_1, fn_2 = f(fn_1 + fn_2), fn_1

def pandigital(n):
	l = []
	while n:
		l.append(n % 10)
		n /= 10
	return check(l)

def first9(n):
	while n >= 1000000000:
		n /= 10
	return n

def last9(n):
	return n % 1000000000

def main():
	limit = 500000
	i = 1
	l = []
	for f_last in fibonacci(last9):
		p_last = pandigital(f_last)
		if p_last:
			l.append(i)
		if i > limit:
			break
		i += 1
	i = 1
	j = 0
	for fn in fibonacci():
		if j >= len(l) or i > limit:
			break
		if i == l[j]:
			if pandigital_first(fn):
				print i
				break
			j += 1
		i += 1

if __name__ == '__main__':
	main()



