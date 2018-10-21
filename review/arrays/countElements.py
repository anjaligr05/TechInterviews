def binSearchCount(arr, target):
	first = -1
	l = 0
	print 'arr = ', arr, 'target = ', target
	r = len(arr)-1
	while l<=r:
		mid = l+(r-l)/2
		if arr[mid]==target:
			first = mid
			r=mid-1
		elif arr[mid]>target:
			r=mid-1
		else:
			l=mid+1
	l = 0
	r = len(arr)-1
	last = -1
	while l<=r:
		mid = l+(r-l)/2
		if arr[mid]==target:
			last = mid
			l = mid+1
		elif arr[mid]>target:
			r = mid-1
		else:
			l = mid+1
	
	return last-first+1
print binSearchCount([1,2,2,3,3,3,3,4,4,4,4,4,4],3)
