def backtrack(ans, curr, arr, remain, k):
	if remain==0 and k==len(curr):
		ans.append(curr)
	if remain<0:
		return
	for i in range(len(arr)):
		if i>0 and arr[i]==arr[i-1]:
			continue
		backtrack(ans, curr+[arr[i]], arr,remain-arr[i], k )
def sum10(arr, target, k):
	ans = []
	backtrack(ans, [],arr,target, k) 
	return ans
print sum10([7,2,3,3], 10, 2)
