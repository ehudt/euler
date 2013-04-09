# problem 66 - take 2

epsilon = 0.000001
from fractions import Fraction
from decimal import Decimal, getcontext
getcontext().prec = 100

def continued_fraction(r, length):
	i = int(r)
	f = Decimal(r - i)
	cont_frac = [i]
	length -= 1
	while length and f > epsilon:
		f_inv = 1/Decimal(f)
		i = int(f_inv)
		f = Decimal(f_inv - i)
		cont_frac.append(i)
		length -= 1
	return cont_frac

def reduce_fraction(cont_frac, start=0):
	if len(cont_frac[start:]) == 1: 
		return cont_frac[start]
	return cont_frac[start] + Fraction(1, reduce_fraction(cont_frac, start + 1))

def convergents(r):
	i = int(r)
	f = r - i
	cont_frac = [i]
	yield reduce_fraction(cont_frac)
	while f > epsilon:
		f_inv = 1/Decimal(f)
		i = int(f_inv)
		f = f_inv - i
		cont_frac.append(i)
		yield reduce_fraction(cont_frac)

def pell_solve(D, x, y):
	return x*x - D*y*y == 1

limit = 1000

def main():
	squares = {x*x for x in xrange(limit + 1)}
	max_x = 0
	max_D = 0
	for D in xrange(limit + 1):
		if D in squares: continue
		for f in convergents(Decimal(D).sqrt()):
			x, y = f.numerator, f.denominator
			if pell_solve(D, x, y):
				if x > max_x:
					max_x = x
					max_D = D
				break
	print max_D

if __name__ == '__main__':
	main()
	
