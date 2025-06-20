"""
数据量过大，不能使用递归，必须使用栈模拟
import sys
from functools import lru_cache
sys.setrecursionlimit(1<<30)

n, m = map(int, input().split())
class Node:
    def __init__(self):
        self.cat = 0
        self.neighbors = []

cats = list(map(int, input().split()))
vertices = [Node() for _ in range(n)]
for i in range(n):
    vertices[i].cat = cats[i]

for _ in range(n-1):
    x, y = map(int, input().split())
    vertices[x-1].neighbors.append(y-1)
    vertices[y-1].neighbors.append(x-1)

cnt = 0
visited = [False]*n

@lru_cache(maxsize = None)
def dfs(node, consecutive_cats):
    global cnt
    visited[node] = True

    if vertices[node].cat == 1:
        consecutive_cats += 1
        if consecutive_cats > m:
            return
    else:
        consecutive_cats = 0

    is_leaf = True
    for neighbor in vertices[node].neighbors:
        if not visited[neighbor]:
            is_leaf = False
            dfs(neighbor, consecutive_cats)

    if is_leaf:
        cnt += 1

dfs(0, 0)
print(cnt)
"""
n, m = map(int, input().split())
class Node:
    def __init__(self):
        self.cat = 0
        self.neighbors = []

cats = list(map(int, input().split()))
vertices = [Node() for _ in range(n)]
for i in range(n):
    vertices[i].cat = cats[i]

for _ in range(n-1):
    x, y = map(int, input().split())
    vertices[x-1].neighbors.append(y-1)
    vertices[y-1].neighbors.append(x-1)

cnt = 0
visited = [False]*n
stack = [(0, 0)]
while stack:
    node, consecutive_cats = stack.pop()
    visited[node] = True
    if vertices[node].cat:
        consecutive_cats += 1
        if consecutive_cats > m:
            continue
    else:
        consecutive_cats = 0
    is_leaf = True
    for neighbor in vertices[node].neighbors:
        if not visited[neighbor]:
            is_leaf = False
            stack.append((neighbor, consecutive_cats))
    if is_leaf:
        cnt += 1
print(cnt)

# CF平台上的数据量太大，能用bfs就不用dfs，不然还要调整成栈模拟比较麻烦