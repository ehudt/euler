#!/usr/bin/env python
# encoding: utf-8
"""
Euler Project Problem 73 - Counting fractions in range

Created by Ehud Tamir on 2013-04-14.
Copyright (c) 2013 Ehud Tamir. All rights reserved.
"""

import sys
import os
from fractions import Fraction
from collections import deque

def add_tup(a, b):
	return tuple(sum(pair) for pair in zip(a, b))

class SternBrocotTree(object):
	"""Iterate on the Stern-Brocot tree.
	@limit	maximum denominator (optional)
	@start	start from the subtree of the given number (optional)"""
	def __init__(self, limit=None, start=None):
		super(SternBrocotTree, self).__init__()
		self.has_limit = limit is not None
		self.limit = limit
		if start:
			frac = Fraction(start)
			self.start = (frac.numerator, frac.denominator)
		else:
			self.start = (2, 5)
		self.current = (2, 5)
		self.lq = (1, 3) # closest smaller ancestor
		self.hq = (1, 2) # closest higher ancestor
		self.queue = deque()
	def check_limit(self, tup):
		''' Check if a tuple (fraction) matches the denominator limit '''
		return not self.has_limit or tup[1] <= self.limit
	def __iter__(self):
		queue = self.queue
		if self.check_limit(self.current):
			queue.append([self.current, self.lq, self.hq])
		while queue:
			current, lq, hq = queue.popleft()
			yield current
			bigger = add_tup(current, hq)
			if self.check_limit(bigger):
				queue.append([bigger, current, hq])
			smaller = add_tup(current, lq)
			if self.check_limit(smaller):
				queue.append([smaller, lq, current])
		


def main():
	tree = SternBrocotTree(limit = 12000)
	print sum(1 for i in tree)


if __name__ == '__main__':
	main()
