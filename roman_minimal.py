# problem 89

roman_numerals = {
 	'I' : 1,
	'V' : 5,
	'X' : 10,
	'L' : 50,
	'C' : 100,
	'D' : 500,
	'M' : 1000,
}

def roman_to_int(roman):
	intify = map(lambda c: roman_numerals[c], roman)
	for i in xrange(len(intify) - 1):
		if intify[i] < intify[i + 1]:
			intify[i] = -intify[i]
	return reduce(lambda x, y: x + y, intify)

ints = { roman_numerals[c] : c for c in roman_numerals }
subtract = { 1000: 100, 500: 100, 100: 10, 50: 10, 10: 1, 5: 1, 1:0 }

def int_to_roman(n):
	roman_out = []
	for value in sorted(ints, reverse=True):
		digits = n / value
		extra = (n + subtract[value]) / value
		roman_out.append(ints[value] * digits)
		if extra - digits:
			roman_out.append(ints[subtract[value]])
			roman_out.append(ints[value])
		n = n - digits * value - (extra - digits) * (value - subtract[value])
		if n == 0: break
	return ''.join(roman_out)

def main():
	input_file = open('roman.txt')
	stripped = [line.strip('\n') for line in input_file]
	print reduce(lambda x, y: x + y, map(lambda x: len(x) - len(int_to_roman(roman_to_int(x))), stripped))

if __name__ == '__main__':
	main()