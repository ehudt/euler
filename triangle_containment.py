# problem 102

import numpy as np
from numpy import linalg
from math import sqrt

""" calculate the projection of a on v """
def projection(a, v):
	return float(np.dot(v, a)) / np.dot(v, v)

def change_basis(a, M):
	return np.dot(linalg.inv(M.T), a)

triangles_input = open('triangles.txt')
z = np.array([0,0])
contain = 0
for line in triangles_input:
	l = map(int, line.strip('\n').split(','))
	a = np.array(l[0:2])
	b = np.array(l[2:4])
	c = np.array(l[4:6])
	x = a - c
	y = b - c
	p = -c
	p_n = change_basis(p, np.array([x,y]))
	print a, b, c, ': ',
	if (p_n >= 0).all() and (p_n > 0).any() and p_n.sum() < 1:
		contain += 1
		print True
	else: print False
print contain

	



