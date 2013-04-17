#!/usr/bin/env python
# encoding: utf-8
"""
Euler Project Problem 206 - Concealed Square

Created by Ehud Tamir on 2013-04-13.
Copyright (c) 2013 Ehud Tamir. All rights reserved.
"""

import sys
import os


def extract_odd_digits(n):
	sgn = 1
	m = 0
	mul = 1
	while n:
		if sgn & 1:
			m += mul * (n % 10)
			mul *= 10
		sgn ^= 1
		n /= 10
	return m

def interleave2nums(n, m):
	mul = 1
	result = 0
	while n or m:
		result += mul * (n % 10) + 10 * mul * (m % 10)
		mul *= 100
		n /= 10
		m /= 10
	result += mul * (n + m)
	return result

import math

def main():
	#print interleave2nums(12345, 10000)
	for i in xrange(1000000000, 0, -10):
		whole = interleave2nums(1234567890, i)
		sqrt_w = int(math.sqrt(whole))
		if not i % 10000000:
			print i
		if sqrt_w*sqrt_w == whole:
			print sqrt_w
			break

if __name__ == '__main__':
	main()

'''
target = 1234567890
for i in xrange(1000000000, 10000000000, 10):
	if extract_odd_digits(i*i) == target:
		print i
		break
'''