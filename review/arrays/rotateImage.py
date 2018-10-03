def antiClockWise(board):
	print board, 'rotating anticlockwise'
	for i in range(len(board)):
		board[i][0], board[i][len(board[i])-1] = board[i][len(board[i])-1], board[i][0]
	for i in range(len(board)):
		for j in range(i+1, len(board[i])):
			board[i][j], board[j][i] = board[j][i], board[i][j]
def clockWise(board):
	print board ,'rotated clockwise :'
	board[0], board[len(board)-1] = board[len(board)-1], board[0]
	for i in range(len(board)):
		for j in range(i+1, len(board[i])):
			board[i][j], board[j][i] = board[j][i], board[i][j]
def rotateImage(board):
	clockWise(board)
	antiClockWise(board)
#board = [[i for i in range(3)] for i in range(3)]
board = [[1,2,3],[4,5,6],[7,8,9]]
rotateImage(board)
print board

