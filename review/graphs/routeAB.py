import collections
import Queue
class Graph:
	def __init__(self):
		self.edges = collections.defaultdict(list)
	def addEdge(self, a, b):
		self.edges[a].append(b)
	def dfsUtil(self, a, b, visited):
		visited[a]=1
		if b==a:
			return True
		for v in self.edges[a]:
			if visited[v]==0:
				if self.dfsUtil(v,b, visited)==True:
					return True
		return False
	def dfs(self, a, b):
		visited = [0 for i in range(4)]
		return self.dfsUtil(a,b, visited)
	def bfs(self, a, b):
		q = Queue.Queue()
		visited = [0 for i in range(4)]
		visited[a] = 1
		q.put(a)
		while q.qsize()>0:
			node = q.get()
			if node==b:
				return True
			for v in self.edges[node]:
				if visited[v]==0:
					visited[v]=1
					q.put(v)
		return False
		
g = Graph()
g.addEdge(0,2)
g.addEdge(0,1)
g.addEdge(1,2)
g.addEdge(2,3)
g.addEdge(3,3)
g.addEdge(2,0)	
print g.dfs(0,3)
print g.bfs(0,3)
