from collections import deque

class Node:
    def __init__(self):
        self.children = list()
        self.in_degree = 0

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    nodes = [Node() for _ in range(n)]
    for _ in range(m):
        x, y = map(int, input().split())
        x -= 1
        y -= 1
        nodes[x].children.append(nodes[y])
        nodes[y].in_degree += 1
    def bfs():
        visited = 0
        q = deque([])
        for node in nodes:
            if node.in_degree == 0:
                q.append(node)
        while q:
            node = q.popleft()
            visited += 1
            for child in node.children:
                child.in_degree -= 1
                if child.in_degree == 0:
                    q.append(child)
        if visited == n:
            return 'No'
        return 'Yes'
    print(bfs())