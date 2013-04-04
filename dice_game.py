# problem 205

from itertools import product
from collections import defaultdict

peter = defaultdict(lambda : 0)

for tup in product(range(1,5), repeat=9):
	peter[sum(tup)] += 1

peter_sum = sum(peter.values())
for key in peter:
	peter[key] = peter[key]/float(peter_sum)

colin = defaultdict(lambda : 0)

for tup in product(range(1,7), repeat=6):
	colin[sum(tup)] += 1

colin_sum = sum(colin.values())
for key in colin:
	colin[key] = colin[key]/float(colin_sum)

prob = 0
for p_key in peter:
	for c_key in colin:
		if p_key > c_key:
			prob += peter[p_key] * colin[c_key]
print prob
