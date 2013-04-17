# problem 82

from sys import maxint

def matrix_from_file(filename):
	with open(filename) as file:
		return [map(int, line.strip('\n').split(',')) for line in file]

def neighbors_maker(rows, cols):
	def neighbors(i, j):
		ret = []
		if i > 0:
			ret.append((i-1, j))
		if i < rows - 1:
			ret.append((i+1, j))
		if j < cols - 1:
			ret.append((i, j+1))
		return ret
	return neighbors

class node(object):
	def __init__(self, distance, row, col):
		super(node, self).__init__()
		self.distance = distance
		self.row = row
		self.col = col
	def __lt__(self, other):
		return self.val() < other.val()
	def __repr__(self):
		return '(%d: %d, %d)' % (self.val(), self.row, self.col)
	def val(self):
		return self.distance[self.row][self.col]

def dijkstra(matrix):
	rows, cols = len(matrix), len(matrix[0])
	visited = [[False]*cols for row in xrange(rows)]
	distance = [[maxint]*cols for row in xrange(rows)]
	heap = []
	neighbors = neighbors_maker(rows, cols)
		
	for i in xrange(rows):
		for j in xrange(cols):
			heap.append(node(distance, i, j))

	for i in xrange(rows):
		distance[i][0] = matrix[i][0]

	while heap:
		heap.sort()
		n = heap.pop(0)
		val, row, col = n.val(), n.row, n.col

		for i, j in neighbors(row, col):
			if not visited[i][j]:
				if distance[i][j] > distance[row][col] + matrix[i][j]:
					distance[i][j] = distance[row][col] + matrix[i][j]

		visited[row][col] = True

	return min(distance[i][cols-1] for i in xrange(rows))


def alt_solution(matrix):
	dim = len(matrix)
	sol = [matrix[i][dim-1] for i in xrange(dim)]
	for j in xrange(dim-2, -1, -1):
		sol[0] += matrix[0][j]
		for i in xrange(1, dim):
			sol[i] = min(sol[i] + matrix[i][j], sol[i-1] + matrix[i][j])
		for i in xrange(dim-2, -1, -1):
			sol[i] = min(sol[i], sol[i+1] + matrix[i][j])
	return min(sol)

def main():
	matrix = matrix_from_file('matrix.txt')
	#print dijkstra(matrix)
	print alt_solution(matrix)

if __name__ == '__main__':
	main()
