class isPermutation():
	def __init__(self, str1, str2):
		print ("{} and {} perm = {}", str1, str2, self.isPermutation(str1, str2))
	def isPermutation(self, str1, str2):
		if len(str1)!=len(str2):
			return False
		for c in str1:
			if str1.count(c)!=str2.count(c):
				return False
		return True
if __name__=='__main__':
	a = isPermutation('hello', 'abc')
	b = isPermutation('loolloeh', 'hello')
	c = isPermutation('    ', ' ')
	d = isPermutation('', '   ')
	e = isPermutation('world','dowrl')
