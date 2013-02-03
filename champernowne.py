def champer(limit):
	count = 0
	i = 0
	l = []
	while count < limit + 2:
		s = str(i)
		l.append(s)
		count += len(s)
		i+= 1
	return ''.join(l)

c = champer(1000000)
l = [c[1], c[10], c[100], c[1000], c[10000], c[100000], c[1000000]]
x = map(int , l)
prod = 1
for i in x:
	prod *= i

print x
print prod