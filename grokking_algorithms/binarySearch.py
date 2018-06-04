class BinarySearch():
	def __init__(self, list, item):
		self.binarySearch(list, item)
	def binarySearch(self, list, item):
		low = 0
		high = len(list)-1
		while low <= high:
			mid = (low+high)/2
			if list[mid] == item:
				print("found {0}, in input ={1} at position {2}".format(item, list, mid))
				return mid
			elif list[mid] < item:
				low = mid+1
			else:
				high = mid-1
		print("not found {0} in input={1}".format(item, list))
		return None
if __name__=='__main__':
	bs = BinarySearch([1,5,8,9,24], 9)
	bs.binarySearch([1,4,6,8,10], 10)
	bs.binarySearch([-5, -4, -3, -1, 0,4], -4)	
	bs.binarySearch([1,4,5], 0)
