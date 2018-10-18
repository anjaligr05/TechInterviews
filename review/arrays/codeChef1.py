def binSearch(arr, val):
	i = 0
	j = len(arr)-1
	endIndex = -1
	while i<=j:
		mid = i+(j-i)/2
		if arr[mid]==val:
			endIndex = mid	
			i = mid+1
		elif arr[mid]>val:
			i =mid+1
		else:
			j=mid-1
	return endIndex	
def qualify(lst, k):
	lst = sorted(lst, reverse=1)
	search = binSearch(lst, lst[k-1])
	return search+1	
N = raw_input()
N = int(N)
ret = []
for i in range(2*N/2):
	nk = raw_input()
	vals = nk.split()
	n = int(vals[0])
	k = int(vals[1])
	lst = raw_input().split()
	lst = [int(x) for x in lst]
	ret.append(qualify(lst, k))
for r in ret:
	print r
	
#print qualify([2,5,5,4,3],1)
#print qualify([6,5,4,3,2,1],4)
	
