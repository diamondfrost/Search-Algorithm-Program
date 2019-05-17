# Bellman-Ford Algorithm -----------------------------------------------------------------------------------------------
from collections import defaultdict, deque, namedtuple

def make_edge(start, end, cost=1):
    return Edge(start, end, cost)


# Class to represent graph
class BFAGraph:
    def __init__(self):
        # checking if data is right
        wrong_edges = [i for i in edges if len(i) not in [2,3]]
        if wrong_edges:
            raise ValueError('Wrong edge data: {}'.format(wrong_edges))
        self.edges = [make_edge(*edge) for edge in edges]

    @property
    def vertices(self):
        return set(
            sum(
                ([edge.start, edge.end] for edge in self.edges), []
            )
        )
    def get_node_pairs(self, n1, n2, both_ends=True):
        if both_ends:
            node_pairs = [[n1, n2], [n2, n1]]
        else:
            node_pairs = [[n1, n2]]
        return node_pairs

    def remove_edge(self, n1, n2, both_ends=True):
        node_pairs = self.get_node_pairs(n1, n2, both_ends)
        edges = self.edges[:]
        for edge in edges:
            if [edge.start, edge.end] in node_pairs:
                self.edges.remove(edge)

    def add_edge(self, n1, n2, cost, both_ends=True):
        node_pairs = self.get_node_pairs(n1, n2, both_ends)
        for edge in self.edges:
            if[edge.start, edge.end] in node_pairs:
                return ValueError('Edge {} {} already exists'.format(n1,n2))

        self.edges.append(Edge(start=n1, end=n2, cost=cost))
        if both_ends:
            self.edges.append(Edge(start=n2, end=n1, cost=cost))

    @property
    def neighbors(self):
        neighbors = {vertex: set() for vertex in self.vertices}
        for edge in self.edges:
            neighbors[edge.start].add((edge.end, edge.cost))
        return neighbors

    # The main function that shortest distances from start to all other vertices.
    # The function also detects negative weight cycle.
    def BellmanFord(self, source, dest):
        # Step 1: Initialize distances from src to all other vertices as INFINITE
        assert source in self.vertices, 'Such source node doesn\'t exist'
        distances = {vertex: inf for vertex in self.vertices}
        previous_vertices = {
            vertex: None for vertex in self.vertices
        }
        distances[source] = 0
        vertices = self.vertices.copy()

        # Step 2: Relax all edges |V| - 1 times.
        # A simple shortest path from start to any other vertex can have at most |V| - 1 edges
        while (vertices - 1):
            current_vertex = min(
                vertices, key=lambda vertex: distances[vertex])
            vertices.remove(current_vertex)
            # Update dist value and parent of the adjacent vertices of the picked vertex.
            # Consider only those vertices which are still in queue.
            for neighbor, cost in self.neighbors[current_vertex]:
                if distances[current_vertex] != float("Inf") and distances[neighbor] + cost < distances[neighbor]:
                    distances[neighbor] = distances[current_vertex] + cost

        # Step 3: check for negative-weight cycles.
        # The above step guarantees shortest distances if graph doesn't contain negative weight cycle.
        # If we get a shorter path, then there is a cycle.
        for neighbor, cost in self.neighbors[current_vertex]:
            if distances[current_vertex] != float("Inf") and distances[neighbor] + cost < distances[neighbor]:
                print ("Graph contains negative weight cycle")
                return

        # print all distances
        print("Vertex Distance from Source")
        for i in range(vertices):
            print("%d \t\t %d" % (i, distances[i]))

BFAgraph = BFAGraph([
    ("START", "A", 1), ("START", "B", 1), ("START", "C", 1), ("START", "D", 1),
    ("A", "A1", 1), ("A", "A2", 1), ("A1", "A3", 1), ("A2", "A3", 1),
    ("B", "B1", 1), ("B1", "B11", 1), ("B1", "B12", 1),
    ("C", "C1", 1), ("C1", "C11", 1),
    ("D", "D1", 1), ("D", "D2", 1), ("D2", "D21", 1),
    ("A1", "AB", 2), ("B1", "AB", 3),
    ("A2", "AC", 2), ("C1", "AC", 4),
    ("B11", "BD", 5), ("D1", "BD", 3)])
