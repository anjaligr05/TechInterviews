def indexOf(haystack, needle):
	print 'haystack = ', haystack, 'needle = ', needle
	nMap = {}
	for i in range(len(needle)):
		nMap[needle[i]]  = nMap.get(needle[i], 0) + 1
	print nMap
	needed = len(nMap)
	for i in range(len(needle)):
		if haystack[i] in nMap:
			nMap[haystack[i]]-=1
			if nMap[haystack[i]]==0:
				needed-=1
				if needed==0:
					return 0
	st = 0
	k = len(needle)
	i = 0
	j = k
	n= len(haystack)
	
	while i<n-k and j<n:
		print haystack[i], haystack[j]
		if haystack[i] in nMap:
			if nMap[haystack[i]] == 0:
				needed+=1
			nMap[haystack[i]]+=1
		if haystack[j] in nMap:	
			nMap[haystack[j]]-=1
			if nMap[haystack[j]]==0:
				needed-=1
			if needed==0:
				return i+1
		i+=1
		j+=1
print indexOf('abcdef','bdc')
print indexOf('hello', 'll')
print indexOf('abcde', 'acdeb')
print indexOf("mississippi","issip")	
