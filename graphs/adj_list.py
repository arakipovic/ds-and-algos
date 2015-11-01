"""Adjacency list graph representation"""


class Vertex(object):
    def __init__(self, uuid, distance=float('inf')):
        self.uuid = uuid
        self.visited = False
        self.neighbors = set()
        self.distance = distance
        self.previous = None

    def add_neighbor(self, neighbor_uuid, distance=1):
        self.neighbors.add(Vertex(neighbor_uuid, distance))

    def __repr__(self):
        return "uuid: {}; visited: {}; neighbors: {}".format(self.uuid, self.visited, [node.uuid for node in self.neighbors])


class AdjListGraph(object):
    def __init__(self, num_vertices):
        self.num_vertices = num_vertices
        self.vertices = [Vertex(uuid) for uuid in range(num_vertices)]

    def add_edge(self, source, destination, cost=1):
        self.vertices[source].add_neighbor(destination, cost)

    def get_edges(self):
        """Return list of tuples (source, destination) vertex uuid."""
        edges = []
        for i in range(self.num_vertices):
            for neigh in self.vertices[i].neighbors:
                    edges.append((i, neigh.uuid))

        return edges


if __name__ == '__main__':
    G = AdjListGraph(5)
    print G.vertices
    G.add_edge(0, 3)
    G.add_edge(1, 2)
    G.add_edge(2, 3)
    G.add_edge(4, 3)
    G.add_edge(2, 1)
    G.add_edge(2, 1)
    print G.vertices
    print G.get_edges()
    v1 = G.vertices[1]
    v1.add_neighbor(2, 5)
    print G.get_edges()
    print v1.neighbors

