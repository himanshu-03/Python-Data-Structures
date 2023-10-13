# Initialize an empty graph
graph = {}

# Function to add an edge to the graph
def add_edge(graph, u, v):
    if u in graph:
        graph[u].append(v)
    else:
        graph[u] = [v]

# Function to print a BFS of a graph
def bfs(graph, start_node):
    if start_node not in graph:
        print("Start node not found in the graph.")
        return

    # Mark vertices as False means not visited
    visited = {node: False for node in graph}

    # Make an empty queue for BFS
    queue = []

    # Mark the given start node as visited and add it to the queue
    visited[start_node] = True
    queue.append(start_node)

    while queue:
        # Remove the front vertex (or the vertex at the 0th index) from the queue and print it.
        v = queue.pop(0)
        print(v, end=" ")

        # Get all adjacent nodes of the removed node v from the graph dictionary.
        # If an adjacent node has not been visited yet, mark it as visited and add it to the queue.
        for neigh in graph[v]:
            if not visited[neigh]:
                visited[neigh] = True
                queue.append(neigh)

# Input from the user to create the graph
while True:
    u = input("Enter the source node (or 'quit' to finish): ")
    if u == 'quit':
        break
    v = input(f"Enter the destination node(s) for node {u} (comma-separated): ")
    for dest in v.split(','):
        add_edge(graph, u, dest)

start_node = input("Enter the start node for BFS: ")
bfs(graph, start_node)
