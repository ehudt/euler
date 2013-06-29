# problem 122

import sys

limit = 200

gen = [None, set()]
weight = [0, 0]

for i in xrange(2, limit + 1):
  min_weight = sys.maxint
  dependence_set = set()
  for a in xrange(1, i):
    b = i - a
    current_weight = 1 + len(gen[a].union(gen[b]))
    if current_weight < min_weight:
      min_weight = current_weight
      dependence_set = gen[a].union(gen[b]).union({a, b})
  weight.append(min_weight)
  gen.append(dependence_set)

print weight[5], gen[5]
print weight[10], gen[10]
print weight[15], gen[15]
print weight[25], gen[25]
print sum(weight[i] for i in xrange(1, limit + 1))