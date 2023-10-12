def create_graph():
    graph = {}
    n = int(input("Enter the number of nodes: "))
    for i in range(n):
        node = str(i)
        edges = set(input(f"Enter the edges for node {node} (space-separated): ").split())
        graph[node] = edges
    return graph

def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)

    print(start)

    for next_node in graph[start] - visited:
        dfs(graph, next_node, visited)
    return visited

graph = create_graph()
start_node = input("Enter the starting node: ")

dfs(graph, start_node)
