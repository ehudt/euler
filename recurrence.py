

def divide10000(divisor):
	remainder = 1
	s = []
	for i in xrange(10000):
		remainder *= 10
		s += str(remainder / divisor)
		remainder %= divisor
	return ''.join(s)

def recurringSince(s, pattern, index):
	search_len = len(s) - index
	ind_range = (search_len / len(pattern)) * len(pattern)
	for i in xrange(index, ind_range, len(pattern)):
		if s.find(pattern, i) != i:
			return False
	return True

def findRecurrenceLength(n):
	dec = divide10000(n)
	for pattern_len in xrange(1, len(dec) / 2 + 1):
		#print 'pattern_len: %d' % pattern_len
		for start_index in xrange(min(100, len(dec) - pattern_len + 1)):
			if recurringSince(dec, dec[start_index : start_index + pattern_len], start_index):
				return pattern_len
d = {}
def main():
	global d
	recurring_len = { 0 : 0 }
	max = 0
	for i in xrange(1, 1000):
		print i
		rec = findRecurrenceLength(i)
		recurring_len[i] = rec
		if rec > recurring_len[max]:
			max = i
	print 'longest occurence in fraction 1/%d of length %d' % (max, recurring_len[max])
	d = recurring_len

if __name__ == '__main__':
	main()