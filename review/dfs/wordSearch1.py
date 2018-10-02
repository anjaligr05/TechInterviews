def dfs(board, i, j, word):
	if len(word)==0:
		return True
	elif i<0 or i>len(board)-1 or j<0 or j>len(board[i])-1 or word[0]!=board[i][j]:
		return False
	temp = board[i][j]
	board[i][j] = '#'
	res = dfs(board, i-1, j, word[1:]) or dfs(board, i+1, j, word[1:]) or dfs(board, i, j-1, word[1:]) or dfs(board, i, j+1, word[1:])
	board[i][j] = temp
	return res
def wordSearch(board, word):
	if not board:
		return False
	print board, 'searching for: ', word
	for i in xrange(0, len(board)):
		for j in xrange(0, len(board[i])):
			if dfs(board, i, j, word):
				return True
	return False
print wordSearch([
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
], "ABCCED")
