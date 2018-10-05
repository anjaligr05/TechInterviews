def isPerfect(num):
	#print num,
	sum =0
	while num>0:
		sum+=num%10
		num/=10
	#print sum
	return sum==10

def nthPerfectNumber(n):
	i = 19
	count = n
	while n>=0:
		if isPerfect(i):
			n-=1
		if n==0:
			return i

		i+=9
#print nthPerfectNumber(2)			
#print nthPerfectNumber(5)
print nthPerfectNumber(1)		
		
