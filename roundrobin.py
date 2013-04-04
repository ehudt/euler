from itertools import cycle, islice


def roundrobin(*iterables):
    "roundrobin('ABC', 'D', 'EF') --> A D E B F C"
    # Recipe credited to George Sakkis
    pending = len(iterables)
    nexts = cycle(iter(it).next for it in iterables)
    while pending:
        try:
            for next in nexts:
                yield next()
        except StopIteration:
            pending -= 1
            nexts = cycle(islice(nexts, pending))

def odd():
	i = 1
	while True:
		yield i
		i += 2

def even():
	i = 0
	while True:
		yield i
		i += 2

r = roundrobin(even(), odd())
print r.next()
print r.next()
print r.next()
print r.next()

print [x for x in roundrobin('ABC', 'D', 'EF')]