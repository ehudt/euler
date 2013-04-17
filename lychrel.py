# problem 55

def reverse(s):
	return s[::-1]

def is_palindrome(s):
	return s == reverse(s)

def lychrel(n):
	for i in xrange(50):
		n = n + int(reverse(str(n)))
		if is_palindrome(str(n)):
			return False
	return True


def main():
	print sum(1 for i in xrange(10000) if lychrel(i))

if __name__ == '__main__':
	main()
