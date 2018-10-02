import math
class TreeNode:
	def __init__(self, val):
		self.val = val
		self.left = None
		self.right = None

def isValidBST(root, maxVal, minVal):
	if root==None:
		return True
	if root.val>minVal and root.val<maxVal:
		return isValidBST(root.left, root.val, minVal) and isValidBST(root.right, maxVal, root.val)
	return False
maxVal = float('inf')
minVal = float('-inf')

root = TreeNode(3)
root.left = TreeNode(1)
root.right = TreeNode(4)
print isValidBST(root, maxVal, minVal)
