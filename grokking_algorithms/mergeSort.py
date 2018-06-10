def mergeSort(arr):
	if len(arr)<2:
		return arr
	mid = len(arr)/2
	larr = arr[:mid]
	rarr = arr[mid:]
	left = mergeSort(larr)
	right = mergeSort(rarr)
	return merge(left, right)
def merge(larr, rarr):
	newarr = []
	i = 0
	j = 0
	while i<len(larr) and j<len(rarr):
		if larr[i]<rarr[j]:
			newarr.append(larr[i])
			i = i+1
		else:
			newarr.append(rarr[j])
			j = j+1
	if i<len(larr):
		for i in range(i, len(larr)):
			newarr.append(larr[i])
	elif j<len(rarr):
		for j in range(j, len(rarr)):
			newarr.append(rarr[j])
	return newarr
print mergeSort([4,7,6,2,8,1])
