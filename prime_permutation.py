from sieve import Sieve
from itertools import combinations

sieve = Sieve(10000)

def permutations(s):
	if s == '':
		yield ''
	for i, c in enumerate(s):
		for perm in permutations(''.join(d for j, d in enumerate(s) if j != i)):
			yield c + perm

for p in sieve:
	if len(str(p)) != 4:
		continue
	p_perm = sorted({x for x in map(int, permutations(str(p))) if sieve.isPrime(x)})
	if len(p_perm) < 3:
		continue
	for combi in combinations(p_perm, 3):
		if (combi[1] - combi[0]) == (combi[2] - combi[1]):
			print combi
			break


