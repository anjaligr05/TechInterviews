def lca(root, n1, n2):
	if root==None:
		return 
	if root.val==n1 or root.val==n2:
		return root
	left = lca(root.left, n1, n2)
	right = lca(root.right, n1, n2)
	if left and right:
		return root
	elif left:
		return left
	else:
		return right
class TreeNode:
	def __init__(self, val):
		self.val = val
		self.left = None
		self.right = None
root = TreeNode(8)
root.left = TreeNode(15)
root.right = TreeNode(19)
root.left.left = TreeNode(4)
root.left.right = TreeNode(6)
print lca(root, 15,19).val
