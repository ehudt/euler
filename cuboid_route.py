# problem 86

import itertools
import math

M = 100
epsilon = 1e-3
count = 0

for j, k, l in itertools.combinations_with_replacement(range(1,M + 1), r=3):
  path = math.sqrt((j + k)**2 + l**2)
  if path - int(path) < epsilon:
    count += 1
'''
for jk, l in itertools.product(range(2, 2*M + 1), range(1,M + 1)):
  path = math.sqrt((jk)**2 + l**2)
  if path - int(path) < epsilon:
    count += (jk - l + 1 - 1)/2 + 1
'''
print count