def backtrack(ans, curr, arr, n):
	if len(curr)==n:
		ans.append(curr)
	for i in range(len(arr)):
		if i>0 and arr[i]==arr[i-1]:
			continue
		backtrack(ans, curr+[arr[i]], arr[:i]+arr[i+1:], n)
def permutations2(arr):
	print 'original arr', arr
	ans = []
	arr.sort()
	backtrack(ans, [], arr, len(arr))
	return ans
print permutations2([2,1,2, 3])
