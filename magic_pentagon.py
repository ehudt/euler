# problem 68

lll = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

from itertools import permutations

def same_sum(l):
	min_out = min(x for x in l if l.index(x) % 2 == 1)
	start = l.index(min_out)
	ll = l + l
	initial_sum = sum(ll[start-1:start+2])
	start += 2
	for i in xrange(4):
		if sum(ll[start-1:start+2]) != initial_sum:
			return False
		start +=2
	return True

def to_string(l):
	min_out = min(x for x in l if l.index(x) % 2 == 1)
	start = l.index(min_out)
	ll = l + l
	s = []
	for i in xrange(5):
		s.append(str(ll[start]) + str(ll[start-1]) + str(ll[start+1]))
		start +=2
	return ''.join(s)




def main():
	max_str = 0
	max_l = []
	for tup in permutations(range(1,10), 9):
		l = list(tup)
		l.insert(1,10)
		if same_sum(l):
			st = to_string(l)
			if (len(st) != 16):
				continue
			str_val = int(to_string(l))
			if str_val > max_str:
				max_str = str_val
				max_l = l

	print max_str
	print max_l

if __name__ == '__main__':
	main()