def matrixLex(matrix):
	print 'original', matrix
	n = len(matrix)
	k = 0
	count = 0
	prev = matrix[0][0]
	flag = 0
	for i in range(len(matrix[0])):
		for j in range(len(matrix)):
			#print prev
			if ord(matrix[j][i])<ord(prev):
				flag=1
			prev = matrix[j][i]
		if flag==1:
			count+=1
			flag = 0
	
	return count
matrix =[['c', 'b', 'a'], ['d', 'a', 'f'], ['g', 'h', 'i']]
m = [['a','b','z','x']]
m1 = [['z','y','x'],['w','v','u'],['t','s','r']]
print matrixLex(matrix)
print matrixLex(m)
print matrixLex(m1)
print matrix
