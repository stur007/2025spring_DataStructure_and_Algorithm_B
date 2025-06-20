from collections import defaultdict
import heapq

n, m = map(int, input().split())
paths = defaultdict(list)
for _ in range(m):
    a, b, c = map(int, input().split())
    paths[a-1].append((b-1, c))
distance = [float('inf') for _ in range(n)]
distance[0] = 0
q = [(0, 0)]
while q:
    cd, cn = heapq.heappop(q)
    if cn == n-1:
        print(cd)
        break
    if cd > distance[cn]:
        continue
    for nn, d in paths[cn]:
        nd = cd + d
        if nd < distance[nn]:
            distance[nn] = nd
            heapq.heappush(q, (nd, nn))