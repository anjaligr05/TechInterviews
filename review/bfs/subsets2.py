def backtrack(ret,arr, curr, index):
	ret.append(curr)
	for i in range(index, len(arr)):
		if i!=index and arr[i]==arr[i-1]:
			continue
		backtrack(ret, arr, curr+[arr[i]], i+1)
def subsets2(arr):
	ret = []
	backtrack(ret, sorted(arr), [], 0)
	return ret
print subsets2([1,1,2])
