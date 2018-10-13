import Queue
class TreeNode:
	def __init__(self, val):
		self.val = val
		self.left = None
		self.right = None
def rightSideView(root):
	queue = Queue.Queue()
	queue.put(root)
	queue.put(None)
	prev = root
	while queue.qsize()>0:
		node = queue.get()
		if node==None:
			print prev.val,
			if queue.qsize()>0:
				print ' '
				queue.put(None)
		else:
			#print node.val,
			prev = node
			if node.left:
				queue.put(node.left)
			if node.right:
				queue.put(node.right)
	
root = TreeNode(3)
root.left = TreeNode(1)
root.left.left = TreeNode(2)
root.left.left.left = TreeNode(6)
root.left.left.right = TreeNode(9)
root.right = TreeNode(4)
root.right.right = TreeNode(7)
root.right.right.right = TreeNode(8)
root.right.right.right.left = TreeNode(10)
rightSideView(root)
