def searchRotated(arr, target):
	i = 0
	j = len(arr)-1
	print arr, 'searching for: ',target 
	while i<=j:
		mid = i+(j-i)/2
		if arr[mid]==target:
			return mid
		if arr[i]<arr[mid] or arr[mid]>arr[j]:
			if target>=arr[i] and target<arr[mid]:
				j = mid-1
			else:
				i=mid+1
		else:
			if target>arr[mid] and target<=arr[j]:
				i = mid+1
			else:
				j = mid-1
	return -1
print searchRotated([4,5,6,0,1,3], 6)
print searchRotated([3,5,7,1,2],5)
print searchRotated([3,5,7,1,2],1)
		
	
