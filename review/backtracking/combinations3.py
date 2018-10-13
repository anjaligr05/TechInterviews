def backtrack(ans, curr, arr, index, remain, k):
	if remain==0 and len(curr)==k:
		ans.append(curr)
	if remain<0:
		return
	for i in range(index, len(arr)):
		backtrack(ans, curr+[arr[i]], arr, i+1, remain-arr[i], k)
def combinations(k, target):
	arr = [i for i in range(1,10)]
	ans = []
	backtrack(ans, [], arr, 0, target, k)
	return ans
print combinations(3, 7)
print combinations(3,9)
