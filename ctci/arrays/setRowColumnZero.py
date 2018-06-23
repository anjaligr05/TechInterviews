def nullifyColumn(matrix, c):
	for i in range(len(matrix)):
		matrix[i][c] = 0
def nullifyRow(matrix, r):
	for j in range(len(matrix[0])):
		matrix[r][j] = 0	
def setToZero(matrix):
	for r in matrix:
		print r
	print('\n')
	firstRowZero = False
	firstColumnZero = False
	for c in range(len(matrix[0])):
		if matrix[0][c]==0:
			firstRowZero = True
	for r in range(len(matrix)):
		if matrix[r][0] == 0:
			firstColumnZero = True
	for i in range(1,len(matrix)):
		for j in range(1,len(matrix[0])):
			if matrix[i][j]==0:
				matrix[0][j]  = 0
				matrix[i][0] = 0
	for e in range(len(matrix[0])):
		if matrix[0][e]==0:
			nullifyColumn(matrix, e)
	for e in range(len(matrix)):
		if matrix[e][0] == 0:
			nullifyRow(matrix, e)
	if firstRowZero:
		nullifyRow(matrix,0)
	if firstColumnZero:
		nullifyColumn(matrix, 0)
	for rows in matrix:
		print rows
setToZero([[1,2,0,1],[2,1,4,1],[2,1,1,0],[5,0,1,2]])
