
def int2bin(n):
	if n == 0:
		return '0'
	output = []
	while n > 0:
		output.append(str(n % 2))
		n /= 2
	return str(''.join(output[::-1]))

def isPalindrome(s):
	return s == s[::-1]

accum = 0
for i in xrange(1000000):
	if isPalindrome(str(i)) and isPalindrome(int2bin(i)):
		accum += i

print accum