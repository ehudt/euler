# problem 57

from fractions import Fraction
from itertools import islice

def expansion():
	denom = Fraction(2)
	while True:
		yield Fraction(1 + 1/denom)
		denom = Fraction(2 + 1/denom)

def main():
	print sum(1 for frac in islice(expansion(), 1000) if len(str(frac.numerator)) > len(str(frac.denominator)))

if __name__ == '__main__':
	main()

