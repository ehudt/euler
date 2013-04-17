from itertools import product

def digit_sum(n):
	return sum(int(s) for s in str(n))

def main():
	print max(digit_sum(a**b) for a, b in product(xrange(100), repeat=2))

if __name__ == '__main__':
	main()