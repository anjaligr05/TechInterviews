def palinPerm(str):
	str = str.replace(" ", "")
 	oneChar = False
	oneCharReq = False
	if len(str)%2 != 0:
		oneCharReq = True
	print 'Input string = ' + str
	visited = []
	for c in str:
		if c not in visited:
			visited.append(c)
			if str.count(c)%2==0:
				continue
			elif str.count(c)%2==1:
				if not oneCharReq:
					print 'no one char req'
					return False
				else:
					if not oneChar:
						oneChar = True
						continue
					else:	
						print 'already see one char'
						return False
			
	return True
def setPalinPerm(str):
	oddCountSet = set()
	print(('Input string : {}').format(str))
	for c in str:
		if str.count(c)%2==0:
			if oddCountSet.contains(c):
				oddCountSet.remove(c)
			else:
				oddCountSet.add(c)
		else:
			oddCountSet.add(c)	
	return len(oddCountSet)<=1
print palinPerm("  taco cat  ")	
print palinPerm("hello")
print palinPerm("hheee")
print palinPerm("a")
print palinPerm('aaa')
print setPalinPerm('aaa')
