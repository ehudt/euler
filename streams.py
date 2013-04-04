
def interleave(gen1, gen2):
	try:
		yield gen1.next()
	except StopIteration:
		for x in gen2:
			yield x
	for x in interleave(gen2, gen1):
		yield x
