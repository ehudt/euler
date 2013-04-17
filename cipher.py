# problem 59

from itertools import product

def toString(cipher):
	return ''.join(map(chr, cipher))

def get_dict():
	f = open("words.txt")
	d = {s.lower().strip('"') for s in f.read().split(',')}
	return d

cipher = []
def main():
	global cipher
	dict = get_dict()
	f = open('cipher1.txt')
	cipher = map(int, f.read().strip('\n').split(','))
	lower_case = [c for c in xrange(ord('a'), ord('z') + 1)]
	for key in product(lower_case, repeat=3):
		new_cipher = list(cipher)
		for i in xrange(len(new_cipher)):
			new_cipher[i] = new_cipher[i] ^ key[i % 3]
		text = toString(new_cipher)
		words = text.strip(',./"\';:-_+=!?$%').split(' ')
		english_words = 0
		for word in words:
			if word.lower() in dict:
				english_words += 1

		if float(english_words)/len(words) > 0.3:
			print key, sum(new_cipher)
			print text

if __name__ == '__main__':
	main()