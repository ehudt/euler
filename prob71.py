
def gcd(a, b):
    """Return greatest common divisor using Euclid's Algorithm."""
    while b:      
        a, b = b, a % b
    return a

def lcm(a, b):
    """Return lowest common multiple."""
    return a * b // gcd(a, b)

def lcmm(*args):
    """Return lcm of args."""   
    return reduce(lcm, args)

from fractions import Fraction

def prev_frac(frac, max_denom):
	max_frac = Fraction(0)
	for d in xrange(1, max_denom + 1):
		lcm_i = lcm(frac.denominator, d)
		new_frac = frac - Fraction(1, lcm_i)
		if new_frac.denominator <= max_denom and new_frac > max_frac:
			max_frac = new_frac
	return max_frac

f = Fraction(3, 7)
f = prev_frac(f, 1000000)
print f
#x = Fraction(1)
#print max((f - Fraction(1, lcm(7, d))) for d in xrange(1,1000001) if 1 <= (f - Fraction(1, lcm(7, d))).denominator <= 1000000)