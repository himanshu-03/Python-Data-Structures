from collections import defaultdict

# Class to represent a graph
class Graph:
    def __init__(self, vertices):
        self.graph = defaultdict(list)  # Dictionary containing adjacency List
        self.V = vertices  # No. of vertices

    # Function to add an edge to the graph
    def addEdge(self, u, v):
        self.graph[u].append(v)

    # A recursive function used by topologicalSort
    def topologicalSortUtil(self, v, visited, stack):
        # Mark the current node as visited.
        visited[v] = True

        # Recur for all the vertices adjacent to this vertex
        for i in self.graph[v]:
            if visited[i] == False:
                self.topologicalSortUtil(i, visited, stack)

        # Push the current vertex to the stack which stores the result
        stack.insert(0, v)

    # The function to do Topological Sort. It uses recursive topologicalSortUtil()
    def topologicalSort(self):
        # Mark all the vertices as not visited
        visited = [False] * self.V
        stack = []

        # Call the recursive helper function to store Topological
        # Sort starting from all vertices one by one
        for i in range(self.V):
            if visited[i] == False:
                self.topologicalSortUtil(i, visited, stack)

        # Print the contents of the stack
        print("Following is a Topological Sort of the given graph:")
        print(stack)

# Input from the user
num_vertices = int(input("Enter the number of vertices: "))
num_edges = int(input("Enter the number of edges: "))

g = Graph(num_vertices)

print("Enter the edges :")
for _ in range(num_edges):
    u, v = map(int, input().split())
    g.addEdge(u, v)

g.topologicalSort()
