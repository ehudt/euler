
f = open("triangle.txt")

l = [map(int, line.split()) for line in f]

for i in xrange(len(l) - 2, -1, -1):
	for j in xrange(len(l[i])):
		l[i][j] = l[i][j] + max(l[i+1][j], l[i+1][j+1])
print l[0][0]