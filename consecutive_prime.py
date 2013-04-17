from sieve import Sieve

def main():
	sieve = Sieve(1000000)
	s = [p for p in sieve]
	max_len = 0
	max_sum = 0
	for i in xrange(len(s) - 1):
		for j in xrange(i + 1, len(s)):
			cons_sum = sum(s[k] for k in xrange(i, j + 1))
			if cons_sum > 1000000:
				break
			cons_len = j - i + 1
			if sieve.isPrime(cons_sum):
				if cons_len > max_len:
					max_len = cons_len
					max_sum = cons_sum
	print max_sum
	print max_len

if __name__ == '__main__':
	main()