def preorder(t1, strn):
	if t1==None:
		return strn.append("X")
	strn.append(str(t1.val))
	preorder(t1.left, strn)
	preorder(t1.right, strn)
def isSubtreePreorder(t1, t2):
	str1 = []
	str2 = []
	preorder(t1, str1)
	preorder(t2, str2)
	return ''.join(str2) in  ''.join(str1)
def isSubtree(t1, t2):
	if t1==None:
		return False
	if t2==None:
		return True
	if t1.val==t2.val and matchTree(t1,t2):
		return True
	else:
		return isSubtree(t1.left, t2) or isSubtree(t1.right, t2)
def matchTree(t1, t2):
	if t1==None and t2==None:
		return True
	if t1==None or t2==None:
		return False
	if t1.val!=t2.val:
		return False
	if t1.val==t2.val and matchTree(t1.left, t2.left) and matchTree(t1.right, t2.right):
		return True
class TreeNode:
	def __init__(self,val):
		self.val = val
		self.left = None
		self.right = None
root = TreeNode(1)
root.left = TreeNode(2)
root.right= TreeNode(3)
root.right.left = TreeNode(4)
root.left.left = TreeNode(5)
root.left.right = TreeNode(6)
t1 = root
root1 = TreeNode(1)
root1.left= TreeNode(2)
root1.left.left = TreeNode(5)
root1.left.left.left = TreeNode(6)
t2 = root1
print isSubtree(t1,root.left)
print isSubtreePreorder(t1,root.left.right)
