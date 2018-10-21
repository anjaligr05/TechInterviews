import math
def squareRoot(num):
	l = 0
	r = num-1
	found = -1
	print 'squarerrot of num = ', num
	if num<2:
		return num
	while l<=r:
		mid = l+(r-l)/2
		#print l, r, mid
		#print mid
		if mid*mid==num:
			return mid
		elif mid*mid>num:
			r = mid-1
		else:	
			found = mid
			l = mid+1
	return found
print squareRoot(26), math.sqrt(26)
print squareRoot(4), math.sqrt(4)
print squareRoot(5)
print squareRoot(7)
print squareRoot(19)
