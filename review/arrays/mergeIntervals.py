def mergeIntervals(intervals):
	print 'intervals original, ', intervals
	ret = [intervals[0]]
	intervals.sort(key = lambda x:x[0])
	first = intervals[0]
	i = 1
	while i<len(intervals):
		#print first
		if intervals[i][0]<=first[1]:
			j = i
			maxj = first[1]
			while j<len(intervals) and intervals[j][0]<=first[1]:
				maxj = max(maxj, intervals[j][1])
				j+=1
			if first[0]<=ret[-1][1]:
				ret.remove(ret[-1])
			ret.append([first[0], maxj])
			first = [first[0], maxj]
			i = j
		else:
			if first not in ret:
				ret.append(first)
			first = intervals[i]
			i+=1
			if i==len(intervals):
				ret.append(intervals[i-1])
	
	return ret
print mergeIntervals([[1,3],[2,6],[8,10],[15,18]])
print mergeIntervals([[1,5],[4,5]])
print mergeIntervals([[1,4],[5,6]])
print mergeIntervals([[4,5],[2,4],[4,6],[3,4],[0,0],[1,1],[3,5],[2,2]])
print mergeIntervals([[2,3],[2,2],[3,3],[1,3],[5,7],[2,2],[4,6]])
