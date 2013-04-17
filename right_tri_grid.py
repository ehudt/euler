# problem 91
from math import sqrt
from itertools import product, combinations
from numpy import allclose

class Point(object):
	"""docstring for Point"""
	def __init__(self, x, y):
		super(Point, self).__init__()
		self.x = float(x)
		self.y = float(y)
	def __sub__(self, other):
		return sqrt((self.x - other.x)**2 + (self.y - other.y)**2)
	def __eq__(self, other):
		return allclose(self - other, 0)
	def __ne__(self, other):
		return self != other
	def __str__(self):
		return "({self.x}, {self.y})".format(self=self)


def main():
	limit = 50
	o = Point(0, 0)
	count = 0
	for p, q in combinations(map(lambda (i, j): Point(i,j), product(range(limit + 1), repeat=2)), 2):
		if p - o == 0 or q - o == 0: continue
		a, b, c = sorted([p-o, q-o, p-q])
		#print p-o, q-o, a, b, c, a*a, b*b, c*c, a*a + b*b == c*c
		if allclose(a*a + b*b, c*c):
			count += 1
	print count

if __name__ == '__main__':
	main()

		
