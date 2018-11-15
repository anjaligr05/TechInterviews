import collections
class Graph:
	def __init__(self):
		self.edges = collections.defaultdict(list)
	def addEdge(self, a, b):
		if b!='':
			self.edges[a].append(b)
		else:
			self.edges[a]=[]
def dfs(node, g, visited, bo):
	visited.add(node)
	for v in g.edges[node]:
		if v not in visited:
			dfs(v, g, visited, bo)
	if node not in bo:
		bo.insert(0,node)
	
def buildOrder(g):
	visited = set()
	bo = []
	for k in g.edges.keys():
		dfs(k,g, visited, bo)
	return bo
 
g=Graph()
g.addEdge('f','c')
g.addEdge('f','b')
g.addEdge('c','a')
g.addEdge('b','a')
g.addEdge('a','e')
g.addEdge('b', 'e')
g.addEdge('b', 'h')
g.addEdge('d', 'g')
print buildOrder(g)
