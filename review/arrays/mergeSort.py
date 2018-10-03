def mergeSort(arr, l, r):
	if l<r:
		mid = l + (r-l)/2
		mergeSort(arr, l, mid)
		mergeSort(arr, mid+1, r)
		merge(arr, l, mid, r)
def merge(arr, l, mid, r):
	left = arr[l:mid+1]
	right = arr[mid+1:r+1]
	i = 0
	j = 0
	k = l
	while i<len(left) and j<len(right):
		if left[i]<=right[j]:
			arr[k] = left[i]
			i+=1
			k+=1
		elif left[i]>right[j]:
			arr[k] = right[j]
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
arr = [4,5,1,2,6,9,10,0]
mergeSort(arr, 0, len(arr)-1)
print arr 
	
