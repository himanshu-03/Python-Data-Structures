import sys
import numpy as np
from collections import defaultdict

class Node():
    def __init__(self, state, parent, action, heuristic):
        self.state = state
        self.parent = parent
        self.action = action
        self.heuristic = heuristic

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
            raise Exception("empty frontier")
        else:
            node = self.frontier[-1]
            self.frontier = self.frontier[:-1]
            return node

class QueueFrontier(StackFrontier):
    def remove(self):
        if self.empty():
            raise Exception("empty frontier")
        else:
            node = self.frontier[0]
            self.frontier = self.frontier[1:]
            return node

class gbfsFrontier(StackFrontier):
    def remove(self):
        if self.empty():
            raise Exception("Empty Frontier")
        else:
            node = min(self.frontier, key=lambda x: x.heuristic)
            self.frontier.remove(node)
            return node

# Create a new class that extends the Graph class
class GBFSGraph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def gbfs(self, start_node, goal_node):
        visited = [False] * (max(self.graph) + 1)
        frontier = gbfsFrontier()
        start_state = Node(start_node, None, None, self.manhattan(start_node, goal_node))
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
                    heuristic = self.manhattan(neighbor, goal_node)
                    neighbor_state = Node(neighbor, node, None, heuristic)
                    frontier.add(neighbor_state)

        return None

    def manhattan(self, node, goal_node):
        x1, y1 = node % 3, node // 3
        x2, y2 = goal_node % 3, goal_node // 3
        return abs(x1 - x2) + abs(y1 - y2)

# Example usage with user input:
gbfs_graph = GBFSGraph()

# Get user input for defining the graph
while True:
    u = int(input("Enter edge source node (or -1 to stop): "))
    if u == -1:
        break
    v = int(input("Enter edge target node: "))
    gbfs_graph.add_edge(u, v)

# Get user input for the start and goal nodes
start_node = int(input("Enter the start node: "))
goal_node = int(input("Enter the goal node: "))

print(f"GBFS starting from node {start_node} to reach node {goal_node}:")
path = gbfs_graph.gbfs(start_node, goal_node)
if path:
    print("Path:", path)
else:
    print("No path found")
