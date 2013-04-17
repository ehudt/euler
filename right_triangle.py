def count_sol(p):
	count = 0
	for i in xrange(1, p):
		for j in xrange(i, p - i - 1):
			if i**2 + j**2 == (p-i-j)**2:
				count +=1
	return count


def main():
	max_count = 0
	max_p = 0
	for p in xrange(3,1001):
		print p
		count = count_sol(p)
		if count > max_count:
			max_count = count
			max_p = p
	print max_p, max_count

if __name__ == '__main__':
	main()