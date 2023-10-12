from collections import defaultdict

class Graph:
    def __init(self):
        self.graph = defaultdict(list)

    def add_edge(self, u, v, cost=1):
        self.graph[u].append((v, cost))

    def bfs(self, start_node):
        visited = [False] * (max(self.graph) + 1)
        queue = []

        queue.append(start_node)
        visited[start_node] = True

        while queue:
            node = queue.pop(0)
            print(node, end=" ")

            for neighbor in self.graph[node]:
                neighbor_node, _ = neighbor
                if not visited[neighbor_node]:
                    queue.append(neighbor_node)
                    visited[neighbor_node] = True

class Node():
    def __init__(self, state, parent, action, heuristic, cost):
        self.state = state
        self.parent = parent
        self.action = action
        self.heuristic = heuristic
        self.cost = cost
        self.combined = heuristic + cost

class StackFrontier():
    def __init__(self):
        self.frontier = []

    def add(self, node):
        self.frontier.append(node)

    def contains_state(self, state):
        return any(node.state == state for node in self.frontier)

    def empty(self):
        return len(self.frontier) == 0

    def remove(self):
        if self.empty():
            raise Exception("Empty frontier")
        else:
            node = self.frontier.pop()
            return node

class QueueFrontier(StackFrontier):
    def remove(self):
        if self.empty():
            raise Exception("Empty frontier")
        else:
            node = self.frontier.pop(0)
            return node

class gbfsFrontier(StackFrontier):
    def remove(self):
        if self.empty():
            raise Exception("Empty Frontier")
        else:
            node = min(self.frontier, key=lambda x: x.heuristic)
            self.frontier.remove(node)
            return node

class a_starFrontier(StackFrontier):
    def remove(self):
        if self.empty():
            raise Exception("Empty Frontier")
        else:
            node = min(self.frontier, key=lambda x: x.combined)
            self.frontier.remove(node)
            return node

class AStarGraph(Graph):
    def a_star(self, start_node, goal_node):
        visited = [False] * (max(self.graph) + 1)
        frontier = a_starFrontier()
        start_state = Node(start_node, None, None, self.manhattan(start_node, goal_node), 0)
        frontier.add(start_state)

        while not frontier.empty():
            node = frontier.remove()
            state = node.state

            if state == goal_node:
                path = []
                while node.parent is not None:
                    path.append(node.state)
                    node = node.parent
                path.append(start_node)
                path.reverse()
                return path

            visited[state] = True

            for neighbor, cost in self.graph[state]:
                if not visited[neighbor]:
                    new_cost = node.cost + cost
                    heuristic = self.manhattan(neighbor, goal_node)
                    neighbor_state = Node(neighbor, node, None, heuristic, new_cost)
                    frontier.add(neighbor_state)

        return None

    def manhattan(self, node, goal_node):
        x1, y1 = node % 3, node // 3
        x2, y2 = goal_node % 3, goal_node // 3
        return abs(x1 - x2) + abs(y1 - y2)

# Example usage with user input:
a_star_graph = AStarGraph()

# Get user input for defining the graph
while True:
    u = int(input("Enter edge source node (or -1 to stop): "))
    if u == -1:
        break
    v = int(input("Enter edge target node: "))
    cost = int(input("Enter edge cost: "))
    a_star_graph.add_edge(u, v, cost)

# Get user input for the start and goal nodes
start_node = int(input("Enter the start node: "))
goal_node = int(input("Enter the goal node: "))

print(f"A* search starting from node {start_node} to reach node {goal_node}:")
path = a_star_graph.a_star(start_node, goal_node)
if path:
    print("Path:", path)
else:
    print("No path found")
