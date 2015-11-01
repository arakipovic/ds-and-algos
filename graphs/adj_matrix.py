"""Adjacency matrix graph representation"""


class Vertex(object):
    def __init__(self, uuid):
        self.uuid = uuid
        self.visited = False

    def add_neighbor(self, graph, neighbor_uuid, cost=1):
        graph.add_edge(self.uuid, neighbor_uuid, cost)

    def get_neighbors(self, graph):
        neighbors = []
        for neighbor_uuid in range(graph.num_vertices):
            if graph.adj_matrix[self.uuid][neighbor_uuid] != float('inf') and graph.adj_matrix[self.uuid][neighbor_uuid] != 0:
                neighbors.append(Vertex(neighbor_uuid))

        return neighbors

    def __repr__(self):
        return "uuid: {}, visited: {}".format(self.uuid, self.visited)


class AdjMatrixGraph(object):
    def __init__(self, num_vertices, initial_cost=float('inf')):
        self.adj_matrix = [[initial_cost]*num_vertices for _ in range(num_vertices)]
        for i in range(num_vertices):
            self.adj_matrix[i][i] = 0
        self.num_vertices = num_vertices
        self.vertices = [Vertex(uuid) for uuid in range(num_vertices)]

    def add_edge(self, source, destination, cost=1):
        self.adj_matrix[source][destination] = cost

    def get_edges(self):
        """Return list of tuples (source, destination) vertex uuid."""
        edges = []
        for i in range(self.num_vertices):
            for j in range(self.num_vertices):
                if self.adj_matrix[i][j] != float('inf') and self.adj_matrix[i][j] != 0:
                    edges.append((i, j))

        return edges


if __name__ == '__main__':
    G = AdjMatrixGraph(5)
    print G.vertices
    G.add_edge(0, 3)
    G.add_edge(1, 3)
    G.add_edge(2, 3)
    G.add_edge(4, 3)
    print G.get_edges()
    v1 = G.vertices[1]
    v1.add_neighbor(G, 2)
    print G.get_edges()
    print v1.get_neighbors(G)

