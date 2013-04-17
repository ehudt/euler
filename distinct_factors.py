from sieve import Sieve
from itertools import combinations

limit = 1000000
#sieve = Sieve(limit)
#print 'Sieve!'

def distinct_prime_factors(n):
	count = 0
	#for p in sieve:
	p = 2
	while n > 1:
		'''if n == 1:
			return count'''
		if n % p == 0:
			count += 1
			while n % p == 0:
				n /= p
		p += 1 if p == 2 else 2
	return count
'''	if n != 1:
		return -1
	else:'''


D = 4
def main():
	consecutive = 0
	i = 1
	first = 0
	while consecutive < D:
		factors = distinct_prime_factors(i)
		if factors < 0:
			print 'Error! not enough primes!'
		if factors == D:
			if consecutive == 0:
				first = i
			consecutive += 1
		else:
			consecutive = 0
		i += 1
	print first

if __name__ == '__main__':
	main()
