def quickSort(arr):
	if len(arr)<2:
		return arr
	mid = len(arr)/2
	pivot = arr[mid]
	less = []
	greater = []
	for i in range(mid):
		if arr[i]<pivot:
			less.append(arr[i])
		else:
			greater.append(arr[i])
	for i in range(mid+1, len(arr)):
		if arr[i]<pivot:
			less.append(arr[i])
		else:
			greater.append(arr[i])
	return quickSort(less) + [pivot] + quickSort(greater)
print quickSort([4,2,1,3,3, 5,3,8, 10])
