class Node:
	def __init__(self, val):
		self.val = val
		self.prev = None
		self.next = None
class LRUCache:
	def __init__(self, capacity):
		self.head = Node(0)
		self.tail = Node(0)
		self.head.next = self.tail
		self.tail.prev = self.head
		self.capacity = capacity
		self.hmap = {}
	def addNode(self, node):
		p = self.tail.prev
		p.next = node
		node.prev = p
		node.next = self.tail
		self.tail.prev = node
	def removeNode(self, node):
		node.prev.next = node.next
		node.next.prev = node.prev
		node.next = None
		node.prev = None

	def get(self, key):
		print 'getting,', key
		node = Node(key)
		if key not in self.hmap:
			return -1
		else:
			self.removeNode(self.hmap[key])
			self.addNode(node)
			return self.hmap[key].val
		
	def put(self, val):
		print 'adding,', val
		node = Node(val)
		if val in self.hmap:
			self.removeNode(node)
			self.hmap.remove(val)
		self.hmap[val] = node
		self.addNode(node)
		if len(self.hmap)> self.capacity:
			del(self.hmap[self.head.next.val])
			self.removeNode(self.head.next)
cache = LRUCache(2)		
cache.put(1)
cache.put(2)
cache.put(3)
cache.put(4)
print cache.get(2)

