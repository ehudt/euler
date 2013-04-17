from fractions import Fraction

def digitCancel(enum, denom):
	orig = Fraction(enum, denom)
	if enum / 10 == denom / 10 and orig == Fraction(enum % 10, denom % 10):
		return True
	if enum % 10 == denom / 10 and orig == Fraction(enum / 10, denom % 10):
		return True
	if enum % 10 == denom % 10 and orig == Fraction(enum / 10, denom / 10):
		return True
	if enum / 10 == denom % 10 and orig == Fraction(enum % 10, denom / 10):
		return True
	return False

def main():
	product = Fraction(1)
	for denom in xrange(11, 100):
		if str(denom).count('0') != 0:
			continue
		for enum in xrange(11, denom):
			if str(enum).count('0') != 0:
				continue
			if digitCancel(enum, denom):
				print '%d/%d' % (enum,denom)
				product *= Fraction(enum, denom)
	print 'Answer:', product

if __name__ == '__main__':
	main()