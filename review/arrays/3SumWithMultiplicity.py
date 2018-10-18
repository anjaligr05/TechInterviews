def _3sumMultip(A, target):
	m = pow(10,9)+7
	A.sort()
	res = 0
	for i in range(len(A)-2):
            isum = target-A[i]
            j = i+1
            k = len(A)-1
            while j < k:
                if A[j] + A[k] > isum:
                    k -= 1
                elif A[j] + A[k] < isum:
                    j += 1
                elif A[j] == A[k]: 
		    n = (k-j+1)
                    res += ((n) * (n-1) / 2)%m
                    break
                else:
                    l =1
                    r = 1
                    while j + 1 < k and A[j] == A[j+1]:
                        l += 1
                        j += 1
                    while k - 1 > j and A[k] == A[k-1]:
                        r += 1
                        k -= 1

                    res += (l*r)%m
                    j += 1
                    k -= 1					
	return res
print _3sumMultip([1,1,2,2,3,3,4,4,5,5],8)
		
				
