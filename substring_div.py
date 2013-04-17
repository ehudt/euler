primes = [2, 3, 5, 7, 11, 13, 17]
def check_condition(s):
	for i in xrange(2, 9):
		prime = primes[i - 2]
		if int(s[i-1:i+2]) % prime != 0:
			return False
	return True

from prime_pandigit import all_permutations

accum = 0
for s in all_permutations([str(x) for x in xrange(10)]):
	if check_condition(s):
		accum += int(s)

print accum