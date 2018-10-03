def mergeSort(arr, l, r):
	inv = 0
	if l<r:
		mid = l+(r-l)/2
		inv =mergeSort(arr,l, mid)
		inv +=mergeSort(arr, mid+1, r)
		inv +=merge(arr, l, mid, r)
	return inv
def merge(arr, l, mid,r):
	left = arr[l:mid+1]
	right = arr[mid+1:r+1]
	i = 0
	j = 0
	inv = 0
	k = l
	while i<len(left) and j <len(right):
		if left[i]<right[j]:
			arr[k] = left[i]
			i+=1
			k+=1
		else:
			arr[k] = right[j]
			inv += len(left)-i
			j+=1
			k+=1
	while i<len(left):
		arr[k] = left[i]
		i+=1
		k+=1
	while j<len(right):
		arr[k] = right[j]
		j+=1
		k+=1
	return inv
print mergeSort([5,4,3,2,1], 0, 4)		
print mergeSort([2,1,0,5,4], 0, 4)
