from math import sqrt

def d(num):
	accum = 1
	for i in xrange(2, int(sqrt(float(num)))):
		if num % i is 0:
			accum += i
			if i * i is not num:
				accum += num / i
	return accum

def isAmicable(num, dnum):
	return num != dnum and num == d(dnum)

def main():
	sum = 0
	amics = {}
	for i in xrange(2, 10000):
		if i in amics:
			continue
		di = d(i)
		if isAmicable(i, di):
			amics[i] = True
			amics[di] = True
			sum += i + di
	print sum

if __name__=='__main__':
	main()