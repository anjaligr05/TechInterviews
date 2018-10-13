import collections
class Graph:
	def __init__(self, vertices):
		self.graph = collections.defaultdict(list)
		self.V = vertices
	def addEdges(self, u, v):
		self.graph[u].append(v)
	def topoSortUtil(self, v, visited, stack):
		print v, self.graph[v]
		visited[v] = True
		for i in self.graph[v]:
			if visited[i]==False:
				self.topoSortUtil(i, visited, stack)
		stack.insert(0, v)
	def topoSort(self):
		visited = [False]*self.V
		stack = []
		for i in range(self.V):
			if visited[i]==False:
				self.topoSortUtil(i, visited, stack)
	
		print stack	
g = Graph(6)
g.addEdges(5,2)
g.addEdges(5,0)
g.addEdges(4,0)
g.addEdges(4,1)
g.addEdges(2,3)
g.addEdges(3,1)
print g.topoSort()	
