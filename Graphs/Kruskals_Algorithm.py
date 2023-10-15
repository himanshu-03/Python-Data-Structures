#Kruskal's Algorithm seeks a minimum spanning tree using a greedy approach.
#Greedy Approach: Selects edges in ascending order of weight, adding them to the MST if they avoid cycles.
#Edge Sorting: Begins by sorting edges by weight in non-decreasing order.
#Disjoint Set Data Structure: Utilizes Union-Find to efficiently manage connected components and prevent cycles.
#Iterative Process: Adds edges to the MST iteratively, starting with the smallest weight edges, until V-1 edges are included (V is the number of vertices).
#Safe Edge Selection: Ensures edges don't create cycles before adding them to the MST.
#Efficiency: Kruskal's Algorithm has O(E log E) time complexity, making it suitable for sparse graphs.
#Applications: Widely used in network design for road networks, electrical circuits, data center connections, and also in clustering and image segmentation.

class KruskalMST:
    def __init__(self, vertices):
        """
        Initialize a KruskalMST object with the given number of vertices.

        Args:
            vertices (int): The number of vertices in the graph.
        """
        self.V = vertices
        self.graph = []

    def add_edge(self, u, v, w):
        """
        Add an edge to the graph.

        Args:
            u (int): The source vertex.
            v (int): The destination vertex.
            w (int): The weight of the edge.
        """
        self.graph.append([u, v, w])

    def find(self, parent, i):
        """
        Find the parent of a vertex using the union-find algorithm.

        Args:
            parent (list): A list representing the parent of each vertex.
            i (int): The vertex to find the parent of.

        Returns:
            int: The parent of the vertex.
        """
        if parent[i] == i:
            return i
        return self.find(parent, parent[i])

    def union(self, parent, rank, x, y):
        """
        Union operation to merge two subsets into one.

        Args:
            parent (list): A list representing the parent of each vertex.
            rank (list): A list representing the rank of each subset.
            x (int): The root of the first subset.
            y (int): The root of the second subset.
        """
        root_x = self.find(parent, x)
        root_y = self.find(parent, y)

        if rank[root_x] < rank[root_y]:
            parent[root_x] = root_y
        elif rank[root_x] > rank[root_y]:
            parent[root_y] = root_x
        else:
            parent[root_x] = root_y
            rank[root_y] += 1

    def kruskal(self):
        """
        Find the minimum spanning tree using Kruskal's algorithm.

        Returns:
            list: A list of edges in the minimum spanning tree, represented as [u, v, w], where u and v are vertices
            and w is the edge weight.
        """
        result = []
        self.graph = sorted(self.graph, key=lambda item: item[2])
        parent = [i for i in range(self.V)]
        rank = [0] * self.V
        i = 0
        e = 0
        while e < self.V - 1:
            u, v, w = self.graph[i]
            i += 1
            x = self.find(parent, u)
            y = self.find(parent, v)
            if x != y:
                e += 1
                result.append([u, v, w])
                self.union(parent, rank, x, y)
        return result


def main():
    """
    Main function to execute the Kruskal's algorithm for finding the Minimum Spanning Tree.

    The function prompts the user for input regarding the number of vertices, number of edges, and edge details.
    It then prints the edges of the Minimum Spanning Tree.
    """
    num_vertices = int(input("Enter the number of vertices: "))
    g = KruskalMST(num_vertices)

    num_edges = int(input("Enter the number of edges: "))
    for _ in range(num_edges):
        u, v, w = map(int, input("Enter edge (u v w): ").split())
        g.add_edge(u, v, w)

    mst = g.kruskal()

    print("Edges in Minimum Spanning Tree:")
    for u, v, w in mst:
        print(f"{u} - {v}: {w}")


if __name__ == "__main__":
    main()

