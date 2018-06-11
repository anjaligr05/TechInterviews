def mergeInPlace(larr, rarr):
	i = 0
	j = 0
	while i<len(larr) and j<len(rarr):
		if larr[i] <= rarr[j]:
			i = i+1
		else:
			temp = larr[i]
			larr[i] = rarr[j]
			i = i+1
			rarr = mergeEle(rarr[j+1:], temp)
	print larr
	print rarr
def mergeEle(arr, temp):
	inilen = len(arr)
	for i in range(len(arr)):
		if arr[i]>temp:
			arr = arr[0:i] + [temp] + arr[i:]
			break
	if len(arr)==inilen:
		arr.append(temp)
	return arr
mergeInPlace([4,5, 7,8, 11],[2,3, 6,6, 10])
def merger(arr1, arr2, m, n):
	for i in range(n-1, -1, -1):
		last = arr1[m-1]
		j=m-2
		while(j>=0 and arr1[j]>arr2[i]):
			arr1[j+1]=arr1[j]
			j = j-1
		if j!=m-2 or last>arr2[i]:
			arr1[j+1] = arr2[i]
			arr2[i]=last
	print arr1
	print arr2
mergeInPlace([4,5, 7,8, 11],[2,3, 6,6, 10])
merger([4,5,7,8,11],[2,3,6,6,10],5,5)
