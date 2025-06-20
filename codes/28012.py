from collections import defaultdict, deque

n = int(input())
edges = defaultdict(list)
for _ in range(n-1):
    a, b = map(int, input().split())
    edges[a].append(b)
    edges[b].append(a)
limited = list(map(int, input().split()))
def bfs():
    q = deque([0])
    visited = set()
    while q:
        node = q.popleft()
        visited.add(node)
        for neighbor in edges[node]:
            if neighbor not in visited and neighbor not in limited:
                q.append(neighbor)
    return len(visited)
print(bfs())