"""BFS and DFS implementations"""
from adj_list import sample_graph
from collections import deque


def dfs(node):
    if node.visited:
        return
    print "visiting: {}".format(node.uuid)
    node.visited = True
    for neigh in node.neighbors:
        dfs(neigh)


def bfs(node):
    Q = deque()
    Q.append(node)
    node.visited = True

    while len(Q) > 0:
        temp = Q.popleft()
        print "visiting: {}".format(temp.uuid)
        for neigh in temp.neighbors:
            if not neigh.visited:
                Q.append(neigh)
                neigh.visited = True


if __name__ == '__main__':
    graph = sample_graph()
    print "DFS:"
    print graph.vertices
    dfs(graph.vertices[0])
    print graph.vertices

    graph = sample_graph()
    print "BFS:"
    print graph.vertices
    bfs(graph.vertices[0])
    print graph.vertices
