# problem 96
# brute force solution alone. slower

def collision(i, j):
	return i/9 == j/9 or (i-j)%9 == 0 or (i/27 == j/27 and (i%9)/3 == (j%9)/3)

def solve(board):
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
		r = solve(b)
		if r:
			return r

def main():
	lines = open('sudoku.txt').read().splitlines()
	total_sum = 0
	while lines:
		lines.pop(0)
		board = []
		for i in xrange(9):
			for x in lines.pop(0):
				board.append(int(x))
		digits3 = solve(board)
		print digits3
		total_sum += digits3
	print total_sum

if __name__ == '__main__':
	main()
