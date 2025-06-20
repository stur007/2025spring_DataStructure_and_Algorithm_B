"""
dfs RE爆栈
import sys
sys.setrecursionlimit(1<<30)

def scope(x, y):
    return 0 <= x<n and 0<=y<m
def dfs(x, y):
    global cnt, visited
    visited[x][y] = True
    cnt += grid[x][y]

    for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
        nx = x + dx
        ny = y + dy
        if scope(nx, ny) and grid[nx][ny] != 0 and not visited[nx][ny]:
            dfs(nx, ny)
"""
from collections import deque
import sys

def scope(x, y):
    return 0 <= x<n and 0<=y<m

def bfs(x, y):
    global visited
    cnt = grid[x][y]
    q = deque([(x, y)])

    while q:
        x, y = q.popleft()

        for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            nx = x + dx
            ny = y + dy
            if scope(nx, ny) and grid[nx][ny] != 0 and (nx, ny) not in visited:
                q.append((nx, ny))
                cnt += grid[nx][ny]
                visited.add((nx, ny))

    return cnt

t = int(sys.stdin.readline())
for _ in range(t):
    n, m = map(int, sys.stdin.readline().split())
    grid = []
    for _ in range(n):
        grid.append(list(map(int, sys.stdin.readline().split())))
    vis = [[False] * m for _ in range(n)]
    ans = 0
    for i in range(n):
        for j in range(m):
            if not vis[i][j] and grid[i][j] != 0:
                vis[i][j] = True  # 标记当前节点已访问
                current = bfs(i, j)
                if current > ans:
                    ans = current
    print(ans)
