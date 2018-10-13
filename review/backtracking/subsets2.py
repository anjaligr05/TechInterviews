def backtrack(ans, curr, arr, index):
	ans.append(curr)
	for i in range(index, len(arr)):
		if i!=index and arr[i]==arr[i-1]:
			continue
		backtrack(ans, curr + [arr[i]], arr, i+1) 
def subsets2(arr):
	print 'original arr with duplicates', arr
	ans = []
	backtrack(ans, [], arr, 0)
	return ans
print subsets2([1,1,2])
print subsets2([1,2,3])
