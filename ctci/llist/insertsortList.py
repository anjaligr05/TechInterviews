class ListNode:
	def __init__(self, val):
		self.val = val
		self.next = None
	def printlist(self, head):
		temp = head
		while temp:
			print temp.val,
			temp = temp.next
		return
def insertionSort(A):
	dummy = ListNode(-1)
	cur = A
	while cur:
		prev = dummy
		while prev.next and prev.next.val<cur.val:
			prev = prev.next
		temp = cur.next
		cur.next = prev.next
		prev.next = cur
		cur = temp
	return dummy.next
head = ListNode(3)
head1 = ListNode(1)
head2 = ListNode(2)
head3 = ListNode(4)
head4 = ListNode(5)
head.next = head1
head1.next = head2
head2.next = head3
head3.next = head4
head.printlist(head)
A = insertionSort(head)
print ""
head.printlist(A)
