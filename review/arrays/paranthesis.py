def paranthesis(paren):
	print 'original, ', paren 
	openB = 0
	closeB = 0
	count = 0
	n = len(paren)
	i = 0
	while i<n:
		if paren[i]=='(':
			openB+=1
			i+=1
		elif paren[i]==')':
			if i==0:
				count+=1
				i+=1
			else:
				if paren[i-1]!='(':
					count+=1
					i+=1
				else:
					openB-=1
					paren=paren[:i-1]+paren[i+1:]
					n = len(paren)
					i = i-1
					#print paren, n, i
	count += openB
	return count
print paranthesis(')))()')
print paranthesis('()(()))')
print paranthesis(')(')	
print paranthesis('(()))))')
