from sieve import Sieve

sieve = Sieve(1000000)
print 'Sieve!'

def isTruncatable(p):
	s = str(p)
	for i in xrange(1, len(s)):
		if not sieve.isPrime(int(s[i:])) or not sieve.isPrime(int(s[:i])):
			return False
	return True

accum = 0
for p in sieve:
	if p < 10:
		continue
	if isTruncatable(p):
		accum += p
		print p

print accum