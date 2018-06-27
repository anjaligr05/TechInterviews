def paraIndex(string, index):
	print "Input string: \'{}\', index:{}".format(string, index)
	firstPtr = -1
	secondPtr = -1
	i = 0
	j = len(string) - 1
	flayer = 0
	blayer = 0
	seen = False
	while i<len(string) and j>=0 and j>=i:
		if string[i]=='(' and not seen:
			flayer +=1
			if index == i:
					seen = True
			i+=1
		else:
			i+=1
		if string[j]==')':
			if flayer>0:
				blayer +=1
				if blayer == flayer:
					return j
				j-=1
		else:
			j-=1
	return -1
print paraIndex("Hello (wprl(d))sdf", 6)		
print paraIndex("Sometimes (when I nest them (my parentheticals) too much (like this (and this))) they get confusing.", 10)
