from collections import deque

n, m = map(int, input().split())
adjacent_nodes = [[] for _ in range(n)]

for _ in range(m):
    u, v = map(int, input().split())
    adjacent_nodes[u].append(v)
    adjacent_nodes[v].append(u)
connected = 'yes'
loop = 'no'
def check():
    global connected, loop
    unvisited = {i for i in range(n)}
    while unvisited:
        element = unvisited.pop()
        q = deque([(-1, element)])
        while q:
            parent, node = q.popleft()
            for neighbor in adjacent_nodes[node]:
                if neighbor not in unvisited:
                    if neighbor != parent:
                        loop = 'yes'
                else:
                    q.append((node, neighbor))
                    unvisited.remove(neighbor)
        if unvisited:
            connected = 'no'
check()
print(f'connected:{connected}')
print(f'loop:{loop}')

# 这个题目看起来简单，其实一点都不难，但是第一次做还是有一点思维量的。如果是有向图是不是会简单一些？