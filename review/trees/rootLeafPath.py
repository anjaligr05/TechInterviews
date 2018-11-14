class TreeNode:
	def __init__(self, val):
		self.val = val
		self.left = None
		self.right = None
def rootLeaf(root, ret, curr):
	if root==None:
		return	
	curr.append(root.val)
	if root and root.left==None and root.right==None:
		ret.append(curr)
		return
	temp = [c for c in curr]
	rootLeaf(root.left, ret,temp)
	temp = [c for c in curr]
	rootLeaf(root.right, ret, temp)
	
def rootToleaf(root):
	if root==None:
		return []
	lst = []
	rootLeaf(root, lst, [])
	return lst
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
print rootToleaf(root)	

