def minimumSubarray(arr, s):
	st = 0
	curSum = 0
	minLen = len(arr)+1
	minlen = ''
	print arr, 'sum>=s: ', s
	for i in range(len(arr)):
		curSum += arr[i]
		if arr[i]>=s:
			print arr[st:i+1]
			return 1
		if curSum>=s:
			while curSum-arr[st]>=s:
				curSum-=arr[st]
				st+=1
			if i-st+1<minLen:
				minLen = i-st+1
				minlen = arr[st:i+1]
			curSum-=arr[st]
			st+=1
	if minLen>len(arr):
		return -1
	else:
		print minlen
		return minLen
print minimumSubarray([2,3,1,2,4,3], 7)
print minimumSubarray([2,3,1,2,4,3], 2)
print minimumSubarray([2,3,1,2,4,3], 8)
