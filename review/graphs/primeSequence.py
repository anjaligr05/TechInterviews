import heapq
def primeSeq(primes, k):
	print 'primes', primes
	ret = set()
	ele = []
	for i in primes:
		heapq.heappush(ele, i)
	c = 0
	while len(ret)<k:
		minE = heapq.heappop(ele)
		ret.add(minE)
		for i in primes:
			heapq.heappush(ele, minE*i)
	return ret
print primeSeq([2,3,5],5)
print primeSeq([3,7,11],5)
print primeSeq([3,11,7],50)
		
