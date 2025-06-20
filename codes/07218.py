from collections import deque

def scope(x, y):
    return 0 <= x <r and 0<= y <c

def bfs(x, y):
    q = deque([(x, y)])
    visited = {(x, y)}
    step = 0
    while q:
        s = len(q)
        for _ in range(s):
            x, y = q.popleft()
            for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                nx = x+dx
                ny = y+dy
                if scope(nx, ny) and maze[nx][ny] != '#' and (nx, ny) not in visited:
                    if maze[nx][ny] == 'E':
                        return step+1
                    q.append((nx, ny))
                    visited.add((nx, ny))
        step += 1
    return  'oop!'
t = int(input())
for _ in range(t):
    r,c = map(int, input().split())
    maze = [input() for _ in range(r)]
    for i in range(r):
        for j in range(c):
            if maze[i][j] == 'S':
                print(bfs(i, j))