# problem 63

counter = 0
for power in xrange(1, 10000):
	for base in xrange(1, 10):
		sexp = str(base**power)
		len_sexp = len(sexp)
		if len_sexp == power:
			counter += 1
print counter
