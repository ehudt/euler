accum = 1
j = 1
dim = 1
for i in xrange(500):
	dim += 2
	j += 2
	for i in xrange(4):
		print j
		accum += j
		j += dim - 1

print accum
