import heapq
from collections import defaultdict
n, m = map(int, input().split())
path = defaultdict(list)
for _ in range(m):
    a, b, w = map(int, input().split())
    path[a].append((b, w))
    path[b].append((a, w))
shortest_path = [(0, 1)]
graph = [float('inf')]*(n+1)
graph[1] = 0
visited = {1:'end'}
def dijkstra():
    while shortest_path:
        c_weight, c_node = heapq.heappop(shortest_path)
        for neighbor, weight in path[c_node]:
                if graph[neighbor] > c_weight + weight:
                    graph[neighbor]  = c_weight + weight
                    heapq.heappush(shortest_path, (graph[neighbor], neighbor))
                    visited[neighbor] = c_node
dijkstra()
if graph[n] != float('inf'):
    ans = []
    node = n
    while node in visited:
        ans.append(node)
        node = visited[node]
    ans.reverse()
    print(*ans)
else:
    print(-1)