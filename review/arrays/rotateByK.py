def rotateByK(arr, k):
	n = len(arr)
	k = k%n
	i = 0
	count = 0
	print arr, 'rotating by k= ', k
	while count<n:
		current = i
		prev = arr[i]
		while True:
			nxt = (current+k)%n
			temp = arr[nxt]
			arr[nxt] = prev
			current = nxt
			prev = temp
			count+=1
			if i==current:
				break
		i+=1
arr = [1,2,3,4,5,6]
rotateByK(arr,2)
print arr
			
