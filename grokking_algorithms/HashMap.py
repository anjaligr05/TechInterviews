class pair():
	def __init__(self, key, val):
		self.key = key
		self.val = val

class HashMap():
	def __init__(self):
		self.store = [0]*15
		self.size = 0
	def get(self, key):
		hashkey = hash(key)
		index = hashkey%15
		if not self.store[index]:
			return None
		else:
			lst = self.store[index]
			if type(lst) == list:
				for i in lst:
					if i.key == key:
						return i.val
			else:
				return self.store[index]
	def put(self, key, val):
		hashkey = hash(key)
		index = hashkey%15
		if not self.store[index]:
			self.store[index] = val
		else:
			lst = self.store[index]
			if type(lst)==list:
				for i in lst:
					if i.key == key:
						flag = 0
						i.val = val
				if flag==1:
					lst.append(pair(key, val))
			else:
				self.store[index] = val
			
h = HashMap()
h.put(3, 2)
h.put(3,4)
h.put("abc", 2)
print h.get(3)
print h.get("abc")	
