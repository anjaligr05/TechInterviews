def backtrack(ret, arr, curr, index):
	ret.append(curr)
	for i in range(index, len(arr)):
		backtrack(ret, arr, curr+[arr[i]], i+1)
	
def subsets(arr):
	ret = []
	backtrack(ret, arr, [],0)
	return ret
print subsets([1,2,3])
