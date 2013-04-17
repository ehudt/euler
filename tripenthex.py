limit = 100000

tri = {n*(n+1)/2 for n in xrange(1, limit)}
pent = {n*(3*n-1)/2 for n in xrange(1, limit)}
hexa = {n*(2*n-1) for n in xrange(1, limit)}

sol = tri.intersection(pent).intersection(hexa)

print sol