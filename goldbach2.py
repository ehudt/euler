from sieve import Sieve
from math import sqrt

sieve = Sieve(10000)

def test_conjecture(n):
	for p in sieve:
		if p > n:
			return False
		base = (n - p) / 2
		if int(sqrt(base))**2 == base:
			return True
	return False

def main():
	i = 9
	while True:
		if not sieve.isPrime(i) and not test_conjecture(i):
			print i
			return
		i += 2

if __name__ == '__main__':
	main()

