from collections import deque
graph = {}
graph = {}
graph['you'] = ['alice', 'bob', 'claire']
graph['bob'] = ['anuj', 'peggy'] 
graph['alice'] = ['peggy'] 
graph['claire'] = ['thom', 'jonny'] 
graph['anuj'] = []
graph['peggy'] = []
graph['thom'] = []
graph['jonny'] = []
def personIsSeller(person):
	if person[-1]=='m':
		return True
	else:
		return False
search_queue = []
search_queue += graph['you']
flag = 0
while search_queue:
	person = search_queue.pop()
	if personIsSeller(person):
		flag = 1
		print(('person {} is seller').format(person))
	else:
		search_queue += graph[person]
if flag == 0:
	print 'Not a mango seller'

