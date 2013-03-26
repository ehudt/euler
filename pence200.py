gcoins = [1, 2, 5, 10, 20, 50, 100, 200]

d = {}

def pence(n, coins=None):
	if coins is None:
		coins = list(gcoins)
	if (str(n) + str(coins)) in d:
		return d[str(n) + str(coins)]
	if n < 0:
		d[str(n) + str(coins)] = 0
		return 0
	if n == 0:
		d[str(n) + str(coins)] = 1
		return 1
	if len(coins) == 0:
		d[str(n) + str(coins)] = 0
		return 0
	accum = 0
	itercoins = list(coins)
	while len(itercoins) > 0:
		#print itercoins
		coin = itercoins.pop(0)
		for val in xrange(1, (n / coin) + 1):
			#print val, coin*val
			accum += pence(n - coin*val, itercoins)
	d[str(n) + str(coins)] = accum
	return accum

