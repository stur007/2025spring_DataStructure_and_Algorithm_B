class Vertex:
    def __init__(self, key):
        self.key = key
        self.neighbors = set()

    def set_neighbor(self, other):
        self.neighbors.add(other)

class Graph:
    def __init__(self):
        self.vertices = dict()

    def set_vertex(self, key):
        self.vertices[key] = Vertex(key)

    def add_edge(self, a, b):
        self.vertices[a].set_neighbor(self.vertices[b])
        self.vertices[b].set_neighbor(self.vertices[a])

    def get_degrees(self, a):
        return len(self.vertices[a].neighbors)

    def check_path(self, a, b):
        return self.vertices[a] in self.vertices[b].neighbors

n, m = map(int, (input().split()))
graph = Graph()
for i in range(n):
    graph.set_vertex(i)
for _ in range(m):
    a, b = map(int, input().split())
    graph.add_edge(a, b)
laplace_matrix = [[0]*n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if i == j:
            laplace_matrix[i][j] = len(graph.vertices[i].neighbors)
        else:
            if graph.check_path(i, j):
                laplace_matrix[i][j] = -1
            else:
                laplace_matrix[i][j] = 0
for i in range(n):
    print(*laplace_matrix[i])
