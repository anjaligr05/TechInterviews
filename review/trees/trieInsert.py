class TrieNode:
	def __init__(self):
		self.children = [None for i in range(26)]
		self.isEndOfWord = 0
class Trie:
	def __init__(self):
		self.root = self.getNode()
	def getNode(self):
		return TrieNode()
	def insert(self, key):
		root = self.root
		length = len(key)
		for level in range(length):
			index = ord(key[level])-ord('a')
			if root.children[index]==None:
				root.children[index] = self.getNode()
			root = root.children[index]
		root.isEndOfWord = 1
	def search(self, key):
		root = self.root
		for level,c in enumerate(key):
			 if root.children[ord(c)-ord('a')]==None:
				return False
			 root = root.children[ord(c)-ord('a')]
		return root!=None and root.isEndOfWord==1
keys = ["the","a","there","anaswe","any", "by","their"] 
output = ["Not present in trie", "Present in tire"] 
  
# Trie object 
t = Trie() 
  
# Construct trie 
for key in keys: 
    print 'inserting key, ', key
    t.insert(key) 	
print("{} ---- {}".format("the",output[t.search("the")])) 		
print("{} ---- {}".format("these",output[t.search("these")]))
