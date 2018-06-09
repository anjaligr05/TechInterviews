def gcd(a, b):
	for i in xrange(min(a,b), 1, -1):
		if a%i==0 and b%i==0:
			return i
	return 1
print gcd(5,6)
print gcd(12,24)
print gcd(1680, 640)
print gcd(4,2)
