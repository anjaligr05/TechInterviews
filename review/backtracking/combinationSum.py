def backtrack(ans, curr, arr, remain, index):
	if remain==0:
		ans.append(curr)
	if remain<0:
		return
	for i in range(index, len(arr)):
		if i>index and arr[i]==arr[i-1]:
			continue
		backtrack(ans, curr+[arr[i]], arr, remain-arr[i], i+1)
def combinationSum(arr, target):
	ans = []
	arr.sort()
	backtrack(ans, [], arr, target, 0)
	return ans
print combinationSum([1,2,5,6],7)
print combinationSum([1,1,5,6],2)
print combinationSum([2,5,1,2],5)
print combinationSum([10,1,2,7,6,1,5], 8)
	
