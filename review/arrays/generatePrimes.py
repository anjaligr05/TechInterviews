import collections
def generatePrimes(k):
	seive = [True]*k
	seive[0] = False
	seive[1] = False
	ret = []
	for i,isPrime in enumerate(seive):
		if isPrime:
			#yield i
			ret.append(i)
			for n in xrange(i*i, k, i):
				seive[n] = False
	return ret
ret = generatePrimes(200)
sPrimes = collections.OrderedDict()
for i in range(len(ret)):
	for j in range(i+1, len(ret)):
		sPrimes[ret[i]*ret[j]] = 1
T = int(raw_input())
ans = []
for i in xrange(T):
	n = int(raw_input())
	seen = False
	for k in sPrimes.keys():
		if n-k in sPrimes:
			ans.append('YES')
			seen = True
			break
	if seen==False:
		ans.append('NO')
for a in ans:
	print a

