class URLify():
	def __init__(self, s, l):
		print('new string = {}', self.urlify(s,l))
	def urlify(self, s, l):
		s = list(s)
		spaces = 0
		last = 0
		for i in range(0,l):
			if s[i] == ' ':
				spaces +=1
		last += l + spaces*2
		print last
		if last > len(s):
			print 'invalid input string'
			return None
		
		for i in range(l-1, -1, -1):
			if s[i]==' ':
				s[last-1] ='0'
				s[last-2] ='2'
				s[last-3] ='%'
				last -=3
			else:
				s[last-1] =s[i]
				
				last -= 1
		print s
		return ''.join(s).strip()
if __name__=='__main__':
	a = URLify("Hello World      ", 12)
			
