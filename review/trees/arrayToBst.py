import Queue
class TreeNode:
	def __init__(self, val):
		self.val = val
		self.left = None
		self.right = None
def createBSTUtil(arr):
	if arr==None or len(arr)==0:
		return None
	if len(arr)==1:
		return TreeNode(arr[0])
	else:
		mid = len(arr)/2
		root = TreeNode(arr[mid])
		left = arr[:mid]
		right = arr[mid+1:]
		root.left = createBSTUtil(left)
		root.right = createBSTUtil(right)
	return root
def inorder(root):
	if root==None:
		return
	inorder(root.left)
	print root.val,
	inorder(root.right)
def printLevelOrder(root):
	q = Queue.Queue()
	q.put(root)
	q.put(None)
	while q.qsize()>0:
		node = q.get()
		
		if node!=None:
			print node.val,
			if node.left:
				q.put(node.left)
			if node.right:
				q.put(node.right)
		else:
			if q.qsize()>0:
				print ''
				q.put(None)
def createBST(arr):
	root = createBSTUtil(arr)
	inorder(root)
	print ''
	printLevelOrder(root)
	print ''
arr = [1,2,3,4,5,6,7,8]
createBST(arr)
	
