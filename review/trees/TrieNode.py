class TrieNode:
	def __init__(self, val):
		self.val = val
		self.children = [None for _ in range(36)]
		self.index = -1
def insert(root, word, index):
	node = root
	for c in word:
		if c.isdigit():
			val = 26+int(c)
		else:
			val = ord(c)-ord('a')
		#print c, val, len(node.children)
		if node.children[val] is None:
			node.children[val] = TrieNode(c)
		node = node.children[val]
	node.index = index
def preorder(root, arr):
	if root is None:
		return
	for i in range(36):
		if root.children[i] != None:
			if root.children[i].index != -1:
				print arr[root.children[i].index]	
			preorder(root.children[i], arr)
	return		

word = 'apple'
word1='apple09'
word2 = 'abcde12'
word3 = 'abcde34'
root = TrieNode('*')
insert(root, word, 0)
insert(root, word1, 1)
insert(root, word2, 2)
insert(root, word3, 3)
preorder(root, [word, word1, word2, word3])	
