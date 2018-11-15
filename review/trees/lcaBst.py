def lca(root, n1, n2):
	if root==None:
		return 
	if root.val==n1 or root.val==n2:
		return root
	if root.val>n1 and root.val>n2:
		return lca(root.left, n1, n2)
	if root.val<n1 and root.val<n2:
		return lca(root.right, n1, n2)
	return root
class TreeNode:
	def __init__(self, val):
		self.val = val
		self.left = None
		self.right = None
root = TreeNode(8)
root.left = TreeNode(5)
root.right = TreeNode(9)
root.left.left = TreeNode(4)
root.left.right = TreeNode(6)
print lca(root, 4,6).val
