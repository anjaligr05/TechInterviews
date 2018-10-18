def spreadWord(arr):
	#print arr
	days = 0
	n = len(arr)
	st = 0
	end = 0
	told = 0
	while st<n and end<n:
		days+=1
		if days==1:
			told+= arr[st]
		else:
			told+=sum(arr[pst+1:end+1])
		end = st+told
		print days, told, arr[st:end+1]
		pst = st
		st = end+1
	return days
print spreadWord([1]*10)
#print spreadWord([5,1,3,2,1])
#print spreadWord([3,4,1,2])
#print spreadWord([1,2,1,1,4])
#print spreadWord([3,2,1,7,1,1,1,1])
#print spreadWord([1,1,1,1])
'''
T = int(raw_input())
ans  = []
for j in range(T):
	N = int(raw_input())
	arr = raw_input().split()
	arr = [int(a) for a in arr]
	ans.append(spreadWord(arr))
for a in ans:
	print a			
'''
