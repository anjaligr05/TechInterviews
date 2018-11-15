class TreeNode:
	def __init__(self, val):
		self.val = val
		self.left = None
		self.right = None
def inOSucc(root, node):
	if root==None:
		return
	print 'root = ', root.val, 'node = ', node.val
	if node.right != None:
		mn = node.right
		while mn:
			mnv = mn.val
			mn = mn.left
		return mnv

	else:
		succ = None
		while root:
			if root.val<=node.val:
				root = root.right
			else:
				succ = root.val
				root = root.left
		return succ
	print 'succ = ', succ
root = TreeNode(8)
root.left = TreeNode(6)
root.left.right = TreeNode(7)
root.left.left = TreeNode(5)
root.right = TreeNode(20)
print inOSucc(root, root.left.right)
			
