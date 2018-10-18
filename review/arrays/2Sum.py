def _2sum(arr, target):
	print 'arr = ', arr, 'target = ', target
	soFar = {}
	for i in range(len(arr)):
		if target - arr[i] in soFar:
			return (soFar[target-arr[i]], i)
		else:
			soFar[arr[i]] = i
	return -1
print _2sum([4,1,2,3], 4)
print _2sum([2,0,-3,-5], -3)
