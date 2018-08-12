class ListNode:
	def __init__(self, val):
		self.val = val
		self.next = None
	def printlist(self, root):
		t = root
		while t:
			print t.val,
			t = t.next
		print ""
		return t
def removeDupsII(A):
	dummy = ListNode(0)
	dummy.next = A
	tail = dummy
	while A:
		cur = A
		while A.next and A.next.val==cur.val:
			A = A.next
		if cur==A:
			tail = tail.next
		else:
			tail.next = A.next
		A = A.next	
	return dummy.next
h = ListNode(1)
h1 = ListNode(1)
h.next = h1
h2 = ListNode(2)
h3 = ListNode(3)
h2.next = h3
h1.next = h2;
h.printlist(h)
print ""
h = removeDupsII(h)
h.printlist(h)
