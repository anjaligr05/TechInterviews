class Node():
	def removeDup(self, head):
		seen = []
		prev = None
		while head:
			if head.val not in seen:
				seen.append(head.val)
				temp = head.next
			else:
				prev.next = head.next
				temp = head.next
				head.next = None
			prev = head
			head = temp
	def printList(self, head):
		while head:
			print head.val,
			head = head.next
		print ""
	def __init__(self, val):
		self.val = val
		self.next = None
if __name__ == '__main__':
	head = Node(5)
	n1 = Node(5)
	n2 = Node(4)
	n3 = Node(1)
	n4 = Node(4)
	n5 = Node(6)
	n6 = Node(7)
	n7 = Node(8)
	head.next = n1
	n1.next = n2
	n2.next = n3
	n3.next = n4
	n4.next = n5
	n5.next = n6
	n6.next = n7
	print "original list"
	head.printList(head)
	print "after removing dupes"
	head.removeDup(head)
	head.printList(head)

		
