def isOneEditAway(str1, str2):
	print("Input strings: {}, {}".format(str1, str2))
	if abs(len(str1) - len(str2)) > 1:
		return False
	len1 = len(str1)
	len2 = len(str2)
	if len1>len2:
		bigger = str1
		smaller = str2
	else:
		smaller = str1
		bigger = str2
	noMatchDone = False
	j = 0
	i = 0
	print smaller, bigger
	while i < len(smaller):
		if smaller[i] != bigger[j]:
			if noMatchDone:
				return False
			else:
				noMatchDone = True
				if len1==len2:
					i+=1
					j+=1
				else:
					j += 1
		else:
			i+=1
			j+=1
	return True
print isOneEditAway('pale', 'ple')
print isOneEditAway('pale', 'bake')
print isOneEditAway('sweet', 'sweat')
print isOneEditAway('ale', 'ale')
