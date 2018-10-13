def binSearch(arr, target):
	i = 0
	j = len(arr)
	print arr, 'searching for :', target
	while i<j:
		mid = i+(j-i)/2
		if arr[mid]<=target:
			i = mid+1
		else:
			j = mid
	print j
	return i-1
print binSearch([0,3,5,10,12],6)
print binSearch([0,3,5,10,12],13)
print binSearch([0,4,6,8,9],4)
