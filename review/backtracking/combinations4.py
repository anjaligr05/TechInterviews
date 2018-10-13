def backtrack(ans, curr, arr, remain):
	if remain==0:
		ans.append(curr)
		#return ans+1
	if remain<0:
		return
	for i in range(len(arr)):
		backtrack(ans, curr+[arr[i]], arr, remain-arr[i])
		#return ans
def combinations(arr, target):
	ans = []
	arr.sort()
	backtrack(ans, [], arr, target)
	print ans
combinations([1,2,3], 4)
