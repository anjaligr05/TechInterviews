def spiralMatrix(n):
	matrix = [[0 for i in range(n)]for i in range(n)]
	rowB = 0
	rowE = n-1
	colB = 0
	colE = n-1
	count = 1
	while rowB<=rowE and colB<=colE:
		#right
		for i in range(colB, colE+1):
			matrix[rowB][i] = count
			count+=1
		rowB+=1
		#down
		for i in range(rowB, rowE+1):
			matrix[i][colE] = count
			count+=1
		colE-=1
		#left
		if rowB<=rowE:
			for i in range(colE,colB-1,-1):
				matrix[rowE][i] = count
				count+=1
		rowE-=1
		#up
		if colB<=colE:
			for i in range(rowE,rowB-1,-1):
				matrix[i][colB] = count
				count+=1
		colB+=1
	return matrix
print spiralMatrix(3)
print spiralMatrix(4)
print spiralMatrix(5)
