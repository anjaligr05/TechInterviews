def dfsUtil(matrix, visited, i, j, r, c):
	visited[i][j] = 1
	lands = [(i-1,j), (i+1,j),(i,j-1),(i,j+1)]
	for l in lands:
		if l[0]<r and l[0]>=0 and l[1]<c and l[1]>=0 and visited[l[0]][l[1]]==0 and matrix[l[0]][l[1]]==1:
			dfsUtil(matrix,visited, l[0],l[1],r,c)
def dfs(matrix, r,c ):
	visited = [[0 for i in range(c)] for j in range(r)]
	count = 0
	for i in range(r):
		for j in range(c):
			if matrix[i][j]==1 and visited[i][j]==0:
				dfsUtil(matrix, visited, i, j, r, c)
				count+=1	
	return count
def numIslands(matrix):
	r = len(matrix)
	c = len(matrix[0])
	return dfs(matrix, r,c)	
matrix = [[1,1,1,1,0],[1,1,0,1,0],[1,1,0,0,0],[0,0,0,0,0]]	
matrix1 = [[1,1,0,0,0],[1,1,0,0,0],[0,0,1,0,0],[0,0,0,1,1]]	
matrix2 = [[1,0,1,0,0],[1,1,0,0,0],[0,0,1,0,0],[0,0,0,1,1]]	
print numIslands(matrix)
print numIslands(matrix1)
print numIslands(matrix2)
