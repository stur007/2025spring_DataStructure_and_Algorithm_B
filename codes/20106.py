import heapq

def scope(x, y):
    return 0<= x < m and 0<= y <n
def dijkstra(a, b, c, d):
    if maze[a][b] == '#' or maze[c][d] == '#':
        return 'NO'
    distance = [(0, a, b)]
    visit = {(a, b): 0}
    while distance:
        current_distance, x, y = heapq.heappop(distance)
        if (x, y) == (c, d):
            return current_distance
        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nx = x+dx
            ny = y+dy
            if scope(nx, ny) and maze[nx][ny] != '#':
                new_distance = current_distance + abs(int(maze[nx][ny])-int(maze[x][y]))
                if (nx, ny) in visit:
                    if visit[(nx, ny)] > new_distance:
                        visit[(nx, ny)] = new_distance
                        heapq.heappush(distance, (new_distance, nx, ny))
                else:
                        visit[(nx, ny)] = new_distance
                        heapq.heappush(distance, (new_distance, nx, ny))
    return 'NO'
m, n, p = map(int, input().split())
maze = []
for _ in range(m):
    maze.append(list(input().split()))
for _ in range(p):
    p, q, r ,s = map(int, input().split())
    print(dijkstra(p, q, r, s))