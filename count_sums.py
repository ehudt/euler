# problem 76

#from pence200 import pence

#print pence(100, coins=range(1,100))

target = 100
sums = [0]*(target + 1)
sums[0] = 1


for i in xrange(1, target):
	for j in xrange(i, target + 1):
		sums[j] += sums[j - i]

print sums[100]