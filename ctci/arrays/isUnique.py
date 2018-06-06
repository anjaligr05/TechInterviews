class isUnique():
	def __init__(self, s):
		print('answer from isunique = {} for i/p s= {}', self.isunique(s), s)
		print('answer from nodsisunique = {}', self.isuniqueNoDs(s))
	def isuniqueNoDs(self, s):
		for c in s:
			if s.count(c)>1:
				return False
		return True
	def isunique(self, s):
		return len(s)==len(set(s))
if __name__=='__main__':
	c = isUnique("hello")
	c = isUnique('abcdef')
	c = isUnique('  ')
