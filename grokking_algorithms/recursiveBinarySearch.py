def recBinarySearch(arr, low, high, k):
	if low<=high:
		mid = low + (high-low)/2
		if arr[mid]==k:
			return mid
		elif arr[mid]>k:
			return recBinarySearch(arr, low, mid-1, k)
		else:
			return recBinarySearch(arr, mid+1, high, k)
	else:
		return -1
print recBinarySearch([1,2,3,4,5],0,4,3)
print recBinarySearch([1,2,4,5],0,3,3)
