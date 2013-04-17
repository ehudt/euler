from sieve import Sieve

sieve = Sieve(1000000)

totient_dict = {}

def totient(n):
	if n in sieve