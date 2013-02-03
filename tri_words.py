triangles = {n*(n+1)/2 for n in xrange(1000)}

def main():
	count = 0
	f = open("words.txt")
	for raw_word in f.read().split(','):
		word = raw_word.strip('"')
		word_sum = sum(ord(s)-ord('A')+1 for s in word)
		if word_sum in triangles:
			count += 1
	print count

if __name__ == '__main__':
	main()