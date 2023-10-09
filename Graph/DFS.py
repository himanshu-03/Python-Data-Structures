'''
--------------- DFS --------------------
-> Time Complexity - O(N) + O(2E) where, N - number of node, E - number of edges
-> This works for both directed and undirected graphs
----------------------------------------
'''

def dfs_helper(graph, node, visited, traversal):
	visited[node] = 1 # mark as visited
	traversal.append(node)

	# traverse the neighbours
	for neighbour in graph[node]:
		if visited[neighbour]!=1:
			traversal = dfs_helper(graph, neighbour, visited, traversal)
	return traversal

# graph - an adjacency list graph, the graph is 0 indexed
def dfs(graph):

    n = len(graph) # number of nodes in graph
    visited = [0 for i in range(n)]
    all_traversals = [] # holds the list of all traversals for all connected components

    for node in range(n):
        if visited[node]==0:
            dfs = dfs_helper(graph, node, visited, [])
            all_traversals.append(dfs)

    return all_traversals 
