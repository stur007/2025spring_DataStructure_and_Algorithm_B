import heapq

p = int(input())
paths = dict()
for _ in range(p):
    paths[input()] = dict()
q = int(input())
for _ in range(q):
    u, v, c = input().split()
    c = int(c)
    paths[u][v] = c
    paths[v][u] = c
r = int(input())
for _ in range(r):
    a, b = input().split()
    visited = {a: 'end'}
    def dijkstra():
        q = [(0, a)]
        distance = dict()
        for place in paths:
            distance[place] = float('inf')
        distance[a] = 0
        while q:
            c_distance, c_place = heapq.heappop(q)
            if c_place == b:
                return
            for neighbor in paths[c_place]:
                    if distance[neighbor]>c_distance+paths[c_place][neighbor]:
                        distance[neighbor] = c_distance+paths[c_place][neighbor]
                        heapq.heappush(q, (distance[neighbor], neighbor))
                        visited[neighbor] = c_place
    dijkstra()
    ans =[]
    while visited[b] != 'end':
        ans.append(b)
        ans.append('('+str(paths[b][visited[b]])+')')
        b = visited[b]
    ans.append(b)
    ans.reverse()
    print('->'.join(ans))