//Prim's Algo to calculate the minimum spanning tree with user-input, using the Fibonacci Heap Method.

import sys
import heapq

class UniqueGraph:
    def __init(self, vertices_count):
        self.V = vertices_count
        self.edges = [[] for _ in range(vertices_count)]

    def find_min_edge(self, key_values, mst_set):
        min_value = sys.maxsize
        min_index = 0

        for vertex in range(self.V):
            if key_values[vertex] < min_value and not mst_set[vertex]:
                min_value = key_values[vertex]
                min_index = vertex

        return min_index

    def find_minimum_spanning_tree(self):
        parents = [None] * self.V
        key_values = [sys.maxsize] * self.V
        key_values[0] = 0
        mst_set = [False] * self.V

        parents[0] = -1
        min_heap = [(0, 0)]

        while min_heap:
            current_value, current_vertex = heapq.heappop(min_heap)
            mst_set[current_vertex] = True

            for edge in self.edges[current_vertex]:
                adjacent_vertex, weight = edge
                if not mst_set[adjacent_vertex] and key_values[adjacent_vertex] > weight:
                    key_values[adjacent_vertex] = weight
                    parents[adjacent_vertex] = current_vertex
                    heapq.heappush(min_heap, (key_values[adjacent_vertex], adjacent_vertex))

        self.print_minimum_spanning_tree(parents, key_values)

    def print_minimum_spanning_tree(self, parents, key_values):
        print("Edge \tWeight")
        for vertex in range(1, self.V):
            print(f"{parents[vertex]} - {vertex}\t{key_values[vertex]}")

# Input the graph from the user
V = int(input("Enter the number of vertices: "))
g = UniqueGraph(V)
print("Enter the edges and their weights (e.g., '1 2 3' means an edge from vertex 1 to vertex 2 with weight 3):")

for _ in range(V - 1):
    u, v, w = map(int, input().split())
    g.edges[u].append((v, w))
    g.edges[v].append((u, w))

g.find_minimum_spanning_tree()
