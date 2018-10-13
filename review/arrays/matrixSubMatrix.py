def printboard(board):
	m = len(board)
	n = len(board[0])
	for i in range(0,m):
		for j in range(n):
			print board[i][j],
		print ' '

def matrixSubMatrix(board):
	m = len(board)
	n = len(board[0])
	printboard(board)
	print ' '
	for i in range(m):
		for j in range(n):
			rowIdx = 3*(i/3)
			colIdx = 3*(i%3)
			#print 'row=', rowIdx, ' col=', colIdx
			print board[rowIdx+j/3][colIdx+j%3],
			print ''

#matrixSubMatrix([[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9]])
matrixSubMatrix([[1,2,3,41,15,16],[4,5,6,7,8,9],[7,8,9,1,2,3]])
