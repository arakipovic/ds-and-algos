from collections import deque
import heapq

from adj_list import sample_graph


def shortest_path_unweighted(start_node):
    """Find shortest path in unweighted graph.

    Finds shortest path from start node to every other node
    in the graph.
    """
    Q = deque()
    Q.append(start_node)
    start_node.visited = True

    while len(Q) > 0:
        temp = Q.popleft()
        for n in temp.neighbors:
            if not n.visited:
                n.distance = temp.distance + 1
                n.visited = True
                n.previous = temp
                Q.append(n)


class Vertex(object):
    def __init__(self, uuid, distance=float('inf')):
        self.uuid = uuid
        self.visited = False
        self.neighbors = set()
        self.distance = distance
        self.previous = None
        self.weights = {}

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

    def add_neighbor(self, neighbor, cost=float('inf')):
        self.neighbors.add(neighbor)
        self.weights.update({neighbor: cost})

    def __repr__(self):
        return "uuid: {}; d: {}".format(self.uuid, self.distance)

    def __str__(self):
        return "uuid: {}; v: {}; d: {}; n: {}; p: {}".format(self.uuid, self.visited, self.distance,
                                                             [node.uuid for node in self.neighbors], self.previous)


class AdjListGraph(object):
    def __init__(self, num_vertices):
        self.num_vertices = num_vertices
        self.vertices = [Vertex(uuid) for uuid in range(num_vertices)]

    def add_edge(self, source, destination, cost=float('inf')):
        neigh = self.vertices[destination]
        if self.vertices[source].weights.get(neigh, float('inf')) >= cost:
            self.vertices[source].add_neighbor(neigh, cost)
            #self.vertices[destination].add_neighbor(self, cost)


class PriorityQueue:
    def __init__(self):
        self._queue = []
        self._index = 0

    def __len__(self):
        return len(self._queue)

    def push(self, item, priority):
        heapq.heappush(self._queue, (priority, self._index, item))
        self._index += 1

    def pop(self):
        return heapq.heappop(self._queue)[-1]


def shortest_path_dijkstra(start_node):
    start_node.distance = 0
    Q = PriorityQueue()
    Q.push(start_node, start_node.distance)

    while len(Q) > 0:
        current = Q.pop()
        #print current

        for neigh in current.neighbors:
            if not neigh.visited and neigh.distance > current.distance + current.weights[neigh]:
                neigh.previous = current
                neigh.distance = current.distance + current.weights[neigh]
                Q.push(neigh, neigh.distance)

        current.visited = True


if __name__ == '__main__':
    graph = sample_graph()
    print "BFS shortest:"
    print graph.vertices
    graph.vertices[0].distance = 0
    shortest_path_unweighted(graph.vertices[0])
    print " ".join(map(str, [node.distance for node in graph.vertices]))
    graph = sample_graph()
    print "Dijkstra shortest:"
    print graph.vertices
    shortest_path_dijkstra(graph.vertices[0])
    print graph.vertices