"""  "defaultdict" in Python
 is a dictionary-like container from the collections
module that provides a default value for keys that do not exist."""

from collections import defaultdict

# Function to run Tarjan's algorithm
def tarjan(graph):

    index = 0
    stack = []
    components = []

    # Track visited and index for each node
    indexes = {}
    lowlinks = {}

    def strongconnect(node):

        # Set the depth index for this node to the smallest unused index
        nonlocal index
        indexes[node] = index
        lowlinks[node] = index
        index += 1
        stack.append(node)

        # Consider successors of `node`
        try:
            successors = graph[node]
        except:

            successors = []
        for successor in successors:
            if successor not in indexes:
                # Successor has not yet been visited; recurse on it
                strongconnect(successor)
                lowlinks[node] = min(lowlinks[node], lowlinks[successor])
            elif successor in stack:
                # Successor is in the stack, hence in the current SCC
                lowlinks[node] = min(lowlinks[node], indexes[successor])

        # If `node` is a root node, pop the stack and generate an SCC
        if lowlinks[node] == indexes[node]:
            connected_component = []

            while True:
                successor = stack.pop()
                connected_component.append(successor)
                if successor == node:
                    break
            components.append(connected_component)

    for node in graph:
        if node not in indexes:
            strongconnect(node)

    return components

# Accept dynamic input for the graph
graph = defaultdict(list)
num_nodes = int(input("Enter the number of nodes: "))
for i in range(num_nodes):
    node = int(input(f"Enter the successors of node {i}: "))
    successors = list(map(int, input().split()))
    graph[node] = successors

print("Strongly Connected Components:")
print(tarjan(graph))



""" Explanation:->

1)  Tarjan's algorithm performs a DFS on the graph to find strongly connected components. 

2) It maintains an index (incremented for each visited node), a stack of visited nodes, and a lowlink value for each node (lowest index reachable from that node).

3) When visiting a node, if any successor is in the stack, the lowlink is updated to be the minimum of its current value and the successor's index. 

4) If the lowlink of a node equals its own index, it is a root node and the current stack represents an SCC. This SCC is popped from the stack and added to the final components list.

5) After Tarjan's finishes, the components list contains all the SCCs in the graph."""