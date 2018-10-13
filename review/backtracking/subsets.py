def backtrack(ans, curr, arr, index):
	ans.append(curr)
	for i in range(index, len(arr)):
		backtrack(ans, curr+[arr[i]],arr, i+1) 
def subsets(arr):
	ans = []
	backtrack(ans, [], arr, 0)
	return ans
print subsets([1,2,3])
