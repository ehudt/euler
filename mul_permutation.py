from collections import Counter

def main():
	i = 1
	while True:
		count = Counter(str(i))
		success = True
		for m in xrange(2, 7):
			if count != Counter(str(i*m)):
				success = False
				break
		if success:
			print i
			break
		i += 1
		
if __name__ == '__main__':
	main()