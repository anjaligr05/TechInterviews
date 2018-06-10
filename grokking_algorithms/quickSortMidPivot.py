def quickSortMidPivot(arr):
	if len(arr)<2:
		return arr
	mid = (len(arr)-1)/2
	pivot = arr[mid]
	less= []
	greater = []
	for i in range(mid):
		if arr[i]<=pivot:
			less.append(arr[i])
		else:
			greater.append(arr[i])
	for i in range(mid+1, len(arr)):
		if arr[i]<=pivot:
			less.append(arr[i])
		else:
			greater.append(arr[i])
	return quickSortMidPivot(less) + [pivot] + quickSortMidPivot(greater)
print quickSortMidPivot([6,3,1,4,5])
