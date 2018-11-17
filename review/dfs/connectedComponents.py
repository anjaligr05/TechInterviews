import collections
class Graph:
	def __init__(self):
		self.edges = collections.defaultdict(list)
	def addEdge(self, a, b):
		if b!= None:
			self.edges[a].append(b)
		else:
			self.edges[a] = []
def dfs(vertex, g, visited):
	visited.add(vertex)
	for node in g.edges[vertex]:
		if node not in visited:
			dfs(node, g, visited)
def connectCom(n, edges):
	g = Graph()
	for i in range(n):
		g.addEdge(i,None)
	for e in edges:
		g.addEdge(e[0],e[1])
		g.addEdge(e[1],e[0])
	visited = set()
	count = 0	
	for k in g.edges.keys():
		if k not in visited:
			dfs(k, g, visited)
			count+=1
	return count
print connectCom(5, [[0,1],[1,2],[3,4]])
print connectCom(5, [[0,1],[1,2],[2,3], [3,4]])
