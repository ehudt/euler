# problem 66

from math import sqrt

limit = 10
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
			#if D in squares or D not in todo:
			#	continue
			sqrt_dio = sqrt(D*y_sqr + 1)
			if sqrt_dio == int(sqrt_dio):
				Ds[D] = int(sqrt_dio)
				todo.remove(D)
				print 'D:', D
				print 'Minimal (x, y):', Ds[D], y
				if Ds[D] > max_x:
					max_x = Ds[D]
					max_D = D
				break
		y_sqr += 2 * y + 1
		y += 1
	print max_D

if __name__ == '__main__':
	main()