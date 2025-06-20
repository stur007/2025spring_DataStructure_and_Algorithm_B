from collections import deque

n = int(input())
m = int(input())
maze = []
visited = set()
for i in range(n):
    s = list(map(int, input().split()))
    maze.append(s)
def scope(x, y):
    return 0<= x <n and 0 <= y <m
def bfs(i, j):
    q = deque([(i, j)])
    visited.add((i, j))
    temp = 1
    step = [(0, -1), (-1, 0), (0, 1), (1, 0)]
    while q:
        x, y = q.popleft()
        for k in range(4):
            if maze[x][y]>>k&1:
                continue
            dx, dy = step[k]
            nx, ny = x+dx, y+dy
            if scope(nx, ny) and (nx, ny) not in visited:
                q.append((nx, ny))
                visited.add((nx, ny))
                temp += 1
    return temp

ans = 0
cnt = 0
for i in range(n):
    for j in range(m):
        if (i, j) not in visited:
            ans = max(ans, bfs(i, j))
            cnt += 1
print(cnt)
print(ans)

# 注意东南西北的定义问题