def urlify(strarr, trueLen):
	j = strarr[:trueLen].count(' ')*2 + trueLen -1
	print j
	for i in range(trueLen-1, -1, -1):
		if strarr[i]==' ':
			strarr[j] ='0'
			strarr[j-1] = '2'
			strarr[j-2] = '%'
			j -= 3
		else:
			strarr[j] = strarr[i]
			j -= 1
	print ''.join(strarr).strip()
	return strarr
urlify(['H','e',' ','l','l',' ',' ', ' ', ' '], 5)

