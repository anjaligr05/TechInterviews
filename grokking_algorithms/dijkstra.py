'''
Graph :   	  A
	      6	/   \ 5
	Start	  |1	Final
	      8	\  / 1
		 B
'''
def createGraph():
	graph = {}
	graph["start"] = {}
	graph["start"]["A"] = 6
	graph["start"]["B"] = 8
	graph["A"]={}
	graph["A"]["Final"] = 5
	graph["A"]["B"] = 1
	graph["B"] = {}
	graph["B"]["Final"] = 1
	graph["Final"] = {}
	return graph
def createcosts():
	infinity = float('inf')
	costs = {}
	costs["A"] = 6
	costs["B"] = 8
	costs["Final"] = infinity
	return costs
def createParents():
	parents = {}
	parents["A"] = "start"
	parents["B"] = "start"
	parents["Final"] = float('inf')
	return parents
def cheapestUnvistiedNode(costs, visited):
	min = float('inf')
	lowest = None
	for node in costs:
		cost = costs[node]
		if cost <= min and node not in visited:
			min = cost
			lowest = node
	return lowest
def dijkstra():
	graph = createGraph()
	costs = createcosts()
	parents = createParents()
	visited = []
	'''
	while there are nodes to process,
	grab the node closest to the start node
	update costs for it's neighbours
	if any of the neighbor's costs were updated, then update it's parents too
	mark this node as visited
	'''
	node = cheapestUnvistiedNode(costs, visited)
	while node is not None:
		print node
		cost = costs[node]
		print cost
		neighbors = graph[node]
		print neighbors
		for n in neighbors.keys():
			newCost = cost + neighbors[n]
			print newCost
			if newCost < costs[n]:
				costs[n]=newCost
				parents[n] = node
		visited.append(node)
		node = cheapestUnvistiedNode(costs, visited)
	print costs
	print parents
dijkstra()	

	
