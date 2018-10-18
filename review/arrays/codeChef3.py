def getSeq(A, B):
	arr = [b-a for a,b in zip(A,B)]
	#print arr
	r = len(arr)-1
	while r>1:
		if arr[r]%3!=0:
			return False
		else:
			last = arr[r]/3
			arr[r] = 0
			arr[r-1] = arr[r-1]-2*last
			arr[r-2] = arr[r-2]-1*last
		#print arr
		r-=1	
	if sum(arr)==0:
		return True
#print getSeq([0,0,0,0,0],[1,2,4,2,3])
#print getSeq([0,0,0,0],[2,5,8,3])
#print getSeq([0,0,0,0,0, 0],[1,5,11,16,12, 9])
T = int(raw_input())
ans = []
for i in range(T):
	N = int(raw_input())
	A = raw_input().split()
	A = [int(a) for a in A]
	B = raw_input().split()
	B = [int(b) for b in B]
	if getSeq(A,B):
		ans.append('TAK')
	else:
		ans.append('NIE')
for a in ans:
	print a

