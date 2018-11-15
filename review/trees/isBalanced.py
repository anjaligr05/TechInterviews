class TreeNode:
	def __init__(self,val):
		self.val = val
		self.left = None
		self.right = None
def height(root):
	if root==None:
		return 0
	return 1 + max(height(root.left), height(root.right))
def isBalanced(root):
	if root == None:
		return True
	return isBalanced(root.left) and isBalanced(root.right) and abs(height(root.left)-height(root.right))<=1
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(8)
print isBalanced(root)
