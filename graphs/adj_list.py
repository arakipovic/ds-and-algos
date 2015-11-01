"""Adjacency list graph representation"""


class Vertex(object):
    def __init__(self, uuid, distance=float('inf')):
        self.uuid = uuid
        self.visited = False
        self.neighbors = set()
        self.distance = distance
        self.previous = None

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.uuid == other.uuid
        return False

    def __ne__(self, other):
        if isinstance(other, self.__class__):
            return self.uuid != other.uuid
        return False

    def __hash__(self):
        return hash(self.uuid)

    def add_neighbor(self, neighbor):
        self.neighbors.add(neighbor)

    def __repr__(self):
        return "uuid: {}; v: {}; d: {}; neighbors: {}".format(self.uuid, self.visited, self.distance, [node.uuid for node in self.neighbors])


class AdjListGraph(object):
    def __init__(self, num_vertices):
        self.num_vertices = num_vertices
        self.vertices = [Vertex(uuid) for uuid in range(num_vertices)]

    def add_edge(self, source, destination, cost=1):
        neigh = self.vertices[destination]
        neigh.distance = cost
        self.vertices[source].add_neighbor(neigh)

    def get_edges(self):
        """Return list of tuples (source, destination) vertex uuid."""
        edges = []
        for i in range(self.num_vertices):
            for neigh in self.vertices[i].neighbors:
                    edges.append((i, neigh.uuid))

        return edges


def sample_graph():
    G = AdjListGraph(9)
    G.add_edge(0, 1)
    G.add_edge(0, 7)
    G.add_edge(0, 4)
    G.add_edge(1, 2)
    G.add_edge(2, 1)
    G.add_edge(2, 3)
    G.add_edge(2, 4)
    G.add_edge(3, 5)
    G.add_edge(3, 6)
    G.add_edge(3, 7)
    G.add_edge(4, 3)
    G.add_edge(4, 5)
    G.add_edge(5, 6)
    G.add_edge(5, 2)
    G.add_edge(5, 3)
    G.add_edge(6, 2)
    G.add_edge(6, 7)
    G.add_edge(6, 7, 5)

    return G

if __name__ == '__main__':
    G = sample_graph()
    print G.vertices
    print G.get_edges()