class Node:
	def __init__(self, val):
		self.val = val
		self.next = None
class LinkedList:
	def __init__(self):
		self.head = None
	def append(self, node):
		'''node = Node(nodeData)'''
		if self.head:
			t = self.head
			while t and t.next:
				t = t.next
			t.next = node
		else:
			self.head = node
	def printList(self, node):
		t = node
		while t:
			print t.val,
			t = t.next
		print ""
def mergeLists(l1, l2):
	temp = None
	if l1 is None:
		return l2
	elif l2 is None:
		return l1
	elif l1.val<=l2.val:
		temp = l1
		temp.next = mergeLists(l1.next, l2)
	else:
		temp = l2
		temp.next = mergeLists(l1, l2.next)
	return temp	
def mergeSort(head):
	if head is None or head.next is None:
		return head

	l1,l2 = divideLists(head)
	l1 = mergeSort(l1)
	l2 = mergeSort(l2)
	head = mergeLists(l1,l2)
	return head
def divideLists(head):
	fast = head
	slow = head
	if fast:
		fast = fast.next
	while fast:
		fast = fast.next
		if fast:
			fast = fast.next
			slow = slow.next
	mid = slow.next
	slow.next = None
	return head, mid
def removeDups(head):
	if head is None or head.next is None:
		return head
	t = head
	prev = head
	t = t.next
	while t:
		temp = t.next
		if t.val == prev.val:
			prev.next = t.next
			t.next = None
		prev = t
		t = temp
	return head
		
if __name__=='__main__':
	lst = LinkedList()
	lst.append(Node(1))
	lst.append(Node(0))
	lst.append(Node(1))
	lst.append(Node(4))
	lst.append(Node(5))
	lst.append(Node(3))
	print 'Original List'
	lst.printList(lst.head)
	head = mergeSort(lst.head)
	print 'no dups'
	head1 = removeDups(head)
	lst.printList(head1)
