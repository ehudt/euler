from collections import defaultdict

def allDigits(s):
	if len(s) != 9:
		return False
	for c in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
		if s.count(c) != 1:
			return False
	return True

def iterateProducts():
	accum = 0
	d = defaultdict(lambda : False)
	for i in xrange(100):
		for j in xrange(100,10000):
			product = i*j
			if d[product]:
				continue
			if allDigits(str(i) + str(j) + str(product)):
				d[product] = True
				accum += product
				print '%d X %d = %d' % (i, j, product)
	print accum

def main():
	iterateProducts()

if __name__ == '__main__':
	main()