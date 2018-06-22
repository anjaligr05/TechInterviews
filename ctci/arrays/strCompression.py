def stringCompression(strn):
	prev = 0
	rep = 0
	count = 0
	newStr = []
	i = 0
	prev = 0
	print('Input string : {}'.format(strn))
	while i< len(strn):
		while i< len(strn)-1 and strn[i]==strn[i+1]:
			i += 1
			count += 1
			prev = i
		if count > 0:
			newStr.append(strn[prev])
			newStr.append(str(count+1))
			count = 0
			prev = i
			i+=1
		else:
			newStr.append(strn[i])
			i+=1
			prev = i
	if len(''.join(newStr))>len(strn):
		return strn
	return ''.join(newStr)
print stringCompression('abaaabbcc')
print stringCompression('aaaa')
print stringCompression('abcde')
