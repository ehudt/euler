# problem 96
# more complex, but faster solution

import heapq
from itertools import product

def getCollisions(board, x, y):
	row = { board[x][j] for j in xrange(9) if j != y }
	column = { board[i][y] for i in xrange(9) if i != x }
	box_x = (x / 3) * 3
	box_y = (y / 3) * 3
	box = { board[i + box_x][j + box_y] for i in xrange(3) for j in xrange(3) if (i, j) != (x, y) }
	collisions = row.union(column).union(box)
	if 0 in collisions:
		collisions.remove(0)
	return collisions

def countZeroes(board):
	sums = 0
	for line in board:
		filtered = filter(lambda x: x==0, line)
		sums += len(filtered)
	return sums

def legalBoard(board):
	for i, j in product(xrange(9), repeat=2):
		if board[i][j] in getCollisions(board, i, j):
			return False
	return True

def deepCopy2D(l):
	return [ list(line) for line in l ]

def allowedMoves(board):
	allowed = [ [{ i for i in range(1, 10) } for j in xrange(9)] for k in xrange(9) ]
	for i, j in product(xrange(9), repeat=2):
		if board[i][j] == 0:
			continue
		current = board[i][j]
		
		for k in xrange(9):
			try:
				allowed[i][j].remove(k)
			except:
				pass
			try:
				allowed[k][j].remove(current)
			except:
				pass
			try:
				allowed[i][k].remove(current)
			except:
				pass
			try:
				x = i/3
				y = j/3
				allowed[3*x+k/3][3*y+k%3].remove(current)
			except:
				pass
			print 'i =', i, 'j =', j, 'k =', k, 'x =', x, 'y =', y, 'curr = ', current
		allowed[i][j].add(current)
	return allowed

def solve(board):
	all_nums = { i for i in xrange(1, 10) }
	while countZeroes(board):
		changed_something = False
		for i in xrange(9):
			for j in xrange(9):
				if board[i][j] != 0:
					continue
				diff = all_nums.difference(getCollisions(board, i, j))
				if len(diff) == 1:
					n = diff.pop()
					board[i][j] = n
					changed_something = True
		if not changed_something: # avoid infinite loop
			break
	if countZeroes(board):
		print 'brute-solving', countZeroes(board)
		b = []
		for line in board:
			for item in line:
				b.append(item)
		b = bruteSolve(b)
		return b
	else:	
		return 100*board[0][0] + 10*board[0][1] + board[0][2]

def collision(i, j):
	return i/9 == j/9 or (i-j)%9 == 0 or (i/27 == j/27 and (i%9)/3 == (j%9)/3)

def bruteSolve(board):
	try:
		z = board.index(0)
	except:
		return 100*board[0] + 10*board[1] + board[2]

	allowed = { 1, 2, 3, 4, 5, 6, 7, 8, 9 }
	for i in xrange(81):
		if board[i] in allowed and collision(i, z):
			allowed.remove(board[i])

	for a in allowed:
		b = list(board)
		b[z] = a
		r = bruteSolve(b)
		if r:
			return r


def main():
	lines = open('sudoku.txt').read().splitlines()
	total_sum = 0
	while lines:
		lines.pop(0)
		board = [ [int(x) for x in lines.pop(0)] for i in xrange(9) ]
		digits3 = solve(board)
		print digits3
		total_sum += digits3
	print total_sum

if __name__ == '__main__':
	main()




'''

def bruteSolve(board):
	all_nums = { i for i in xrange(1, 10) }
	zeroes = [(x, y) for x in xrange(9) for y in xrange(9) if board[x][y] == 0]
	print len(zeroes)
	for values in map(list, product(xrange(9), repeat=len(zeroes))):
		failed = False
		for i, j in zeroes:
			value = values.pop()
			if value in getCollisions(board, i, j):
				failed = True
				break
			board[i][j] = value
		if failed:
			continue
		if legalBoard(board):
			return board

	return [[] for i in xrange(9)]



def bruteSolve(board):
	all_nums = { i for i in xrange(1, 10) }

	def helper(board):
		if countZeroes(board) == 0:
			return True, board
		for i, j in product(xrange(9), repeat=2):
			if board[i][j] != 0:
				continue
			diff = all_nums.difference(getCollisions(board, i, j))
			if not diff:
				return False, board
			for n in diff:
				new_board = deepCopy2D(board)
				new_board[i][j] = n
				status, ret_board = helper(new_board)
				if status:
					return status, ret_board
		return False, []
	status, board = helper(board)
	return board
'''