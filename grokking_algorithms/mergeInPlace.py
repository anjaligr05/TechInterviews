def mergeInPlace(larr, rarr):
	i = 0
	j = 0
	while i<len(larr) and j<len(rarr):
		if larr[i] <= rarr[j]:
			i = i+1
		else:
			temp = larr[i]
			larr[i] = rarr[j]
			i = i+1
			rarr = mergeEle(rarr[j+1:], temp)
	print larr
	print rarr
def mergeEle(arr, temp):
	inilen = len(arr)
	for i in range(len(arr)):
		if arr[i]>temp:
			arr = arr[0:i] + [temp] + arr[i:]
			break
	if len(arr)==inilen:
		arr.append(temp)
	return arr
mergeInPlace([4,5, 7,8, 11],[2,3, 6,6, 10])

