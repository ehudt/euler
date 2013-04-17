from fractions import Fraction

def coeff(n):
	if n == 1:
		return 2
	n -= 2
	if n % 3 != 1:
		return 1
	else:
		return ((n / 3) + 1) * 2

def nth_convergent(n, remainder=Fraction(0)):
	if n == 1:
		return Fraction(2) + remainder
	else:
		return nth_convergent(n - 1, Fraction(1, coeff(n) + remainder))

print nth_convergent(100)
print sum(int(s) for s in str(nth_convergent(100).numerator))