def backtrack(ans, curr, arr, n):
	if len(curr)==n:
		ans.append(curr)
	else:
		for i in range(len(arr)):
			backtrack(ans, curr+[arr[i]], arr[:i]+arr[i+1:], n)
def permutations(arr):
	ans = []
	print 'original arr = ', arr
	backtrack(ans, [], arr, len(arr))
	return ans
print permutations([1,2,4])
