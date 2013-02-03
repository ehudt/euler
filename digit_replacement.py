from sieve import Sieve
from itertools import combinations

sieve = Sieve(1000000)

def iterate_replacements(s, combi):
	for j in xrange(10):
		c = str(j)
		ret = [(ch if ind not in combi else c) for ind, ch in enumerate(s)]
		yield ''.join(ret)

def main():
	for p in sieve:
		s = str(p)
		for i in xrange(1, len(s)):
			for combi in combinations((x for x in xrange(len(s) - 1)), i):
				count = 0
				for repl in iterate_replacements(s, combi):
					if len(str(int(repl))) < len(s):
						continue
					if sieve.isPrime(int(repl)):
						count += 1
				if count == 8:
					for repl in iterate_replacements(s, combi):
						if len(str(int(repl))) < len(s) or not sieve.isPrime(int(repl)): 
							continue
						print repl
						break

if __name__ == '__main__':
	main()
