# problem 77

from pence200 import pence
from sieve import Sieve

for i in xrange(100):
	if pence(i, coins=list(Sieve(200))) > 5000:
		print i
		break