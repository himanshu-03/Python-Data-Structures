from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def bfs(self, start_node):
        visited = [False] * (max(self.graph) + 1)
        queue = []

        queue.append(start_node)
        visited[start_node] = True

        while queue:
            node = queue.pop(0)
            print(node, end=" ")

            for neighbor in self.graph[node]:
                if not visited[neighbor]:
                    queue.append(neighbor)
                    visited[neighbor] = True

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

# Create a new class that extends the Graph class for A* search
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

            for neighbor in self.graph[state]:
                if not visited[neighbor]:
                    cost = node.cost + 1  # Assuming unit cost for simplicity
                    heuristic = self.manhattan(neighbor, goal_node)
                    neighbor_state = Node(neighbor, node, None, heuristic, cost)
                    frontier.add(neighbor_state)

        return None

    def manhattan(self, node, goal_node):
        x1, y1 = node % 3, node // 3
        x2, y2 = goal_node % 3, goal_node // 3
        return abs(x1 - x2) + abs(y1 - y2)

# Example usage:
a_star_graph = AStarGraph()
a_star_graph.add_edge(0, 1)
a_star_graph.add_edge(0, 2)
a_star_graph.add_edge(1, 2)
a_star_graph.add_edge(2, 0)
a_star_graph.add_edge(2, 3)
a_star_graph.add_edge(3, 3)

goal_node = 3
print("A* search starting from node 2 to reach node 3:")
path = a_star_graph.a_star(2, goal_node)
if path:
    print("Path:", path)
else:
    print("No path found")
