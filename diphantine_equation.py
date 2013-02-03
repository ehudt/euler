# problem 66

from math import sqrt
import gmpy

limit = 1000
squares = {x*x : x for x in xrange(limit + 1)}
Ds = {}
todo = {d for d in xrange(1, limit + 1) if d not in squares}

def main():
	max_D = 0
	max_x = 0
	y = 1
	y_sqr = 1
	while len(todo) > 0:
		for D in list(todo):
			if gmpy.is_square(D*y_sqr + 1):
				int_sqrt = int(sqrt(D*y_sqr + 1))
				Ds[D] = int_sqrt
				todo.remove(D)
				print 'D:', D
				print 'Minimal (x, y):', int_sqrt, y
				if int_sqrt > max_x:
					max_x = int_sqrt
					max_D = D
		y_sqr += 2 * y + 1
		y += 1
	print max_D

if __name__ == '__main__':
	main()