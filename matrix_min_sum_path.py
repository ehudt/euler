# problem ??

matrix_file = open("matrix.txt")
matrix = [map(int, line.split(',')) for line in matrix_file]
#min_sums = [list(line) for line in matrix]
for i in xrange(1, len(matrix)):
	matrix[i][0] += matrix[i-1][0]
for j in xrange(1, len(matrix[0])):
	matrix[0][j] += matrix[0][j-1]

for i in xrange(1, len(matrix)):
	for j in xrange(1, len(matrix[0])):
		matrix[i][j] += min(matrix[i-1][j], matrix[i][j-1])
ind = len(matrix) - 1
print matrix[ind][ind]