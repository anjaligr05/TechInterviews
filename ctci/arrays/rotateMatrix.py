def rotateClock(matrix):
	for r in matrix:
		print r
	print 'Clockwise rotation\n'
	for layer in range(len(matrix)/2):
		first = layer
		last = len(matrix)-layer-1
		for i in range(first, last):
			offset = i - first
			'''
			left->top
			bottom->left
			right->bottom
			save top in right'''
			temp = matrix[first][i]
			matrix[first][i] = matrix[last-offset][first]
			matrix[last-offset][first] = matrix[last][last-offset]
			matrix[last][last-offset] = matrix[i][last]
			matrix[i][last] = temp
	for r in matrix:
		print r
def rotateAntiClock(matrix):
	for r in matrix:
		print r
	print "Anti Clockwise \n"
	for layer in range(len(matrix)/2):
		first = layer
		last = len(matrix)-1-layer
		for i in range(first, last):
			offset = i-first
			'''
			save top
			right->top
			botton->right
			left->bottom
			save top in left'''
			temp = matrix[first][i]
			matrix[first][i] = matrix[i][last]
			matrix[i][last] = matrix[last][last-offset]
			matrix[last][last-offset] = matrix[last-offset][first]
			matrix[last-offset][first] = temp
	for r in matrix:
		print r
rotateClock([[1,2,3],[3,4,5],[2,6,8]])
print "\n"
rotateAntiClock([[1,2,6],[3,4,7],[3,7,2]])
