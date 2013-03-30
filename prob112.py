def sgn(n):
	return n/abs(n) if n != 0 else 0

def right_digits_sign(n):
	first = n % 10
	second = (n/10)%10
	#print second, first
	#print sgn(n % 10 - (n / 10)%10)
	return sgn(n % 10 - (n / 10)%10)

def is_bouncy(n):
	if n < 100: return False
	sign = right_digits_sign(n)
	while not sign:
		if n == 0: return True
		n /= 10
		sign = right_digits_sign(n)

	while n >= 100:
		n /= 10
		next_sign = right_digits_sign(n)
		if next_sign != sign and next_sign != 0:
			return True
	return False

proportion = 0.

count = 0
bouncy = 0
i = 0

while proportion < 0.99:
	count += 1
	i += 1
	bouncy += is_bouncy(i)
	proportion = float(bouncy)/count

print i, proportion