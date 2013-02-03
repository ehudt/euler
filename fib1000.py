
class FibIter(object):
	"""Fibonacci sequence iterator"""
	def __init__(self):
		super(FibIter, self).__init__()
		self.a = 0
		self.b = 1
		self.term = 0
	def next(self):
		""" Get the next fibonacci number in the sequence """
		ret_val = self.b
		self.b = self.a + self.b
		self.a = ret_val
		self.term += 1
		return ret_val
	def getTerm(self):
		return self.term

def main():
	fib = FibIter()
	num_len = 0
	while num_len < 1000:
		f = fib.next()
		num_len = len(str(f))
		if num_len == 1000:
			print fib.getTerm()

if __name__ == '__main__':
	main()