def quickSort(arr):
	if len(arr)<2:
		return arr
	pivot = arr[0]
	less  = [i for i in arr[1:] if i<=pivot]
	greater = [i for i in arr[1:] if i>pivot]
	return quickSort(less) + [pivot] + quickSort(greater)
print quickSort([6,3,1,4,5])
