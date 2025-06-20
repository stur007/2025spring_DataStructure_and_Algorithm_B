def scope(x, y):
    return 0 <= x < n and 0 <= y < m
def dfs(x, y, temp, visited):
    global cnt

    if len(temp) == n * m:
        cnt += 1
        return

    for dx, dy in [(1, 2), (1, -2), (-1, 2), (-1, -2), (2, 1), (2, -1), (-2, 1), (-2, -1)]:
        nx = x + dx
        ny = y + dy
        if scope(nx, ny) and not visited[nx][ny]:
            temp.append((nx, ny))
            visited[nx][ny] = True
            dfs(nx, ny, temp, visited)
            visited[nx][ny] = False
            temp.pop()

t = int(input())
for _ in range(t):
    n, m, x, y = map(int, input().split())
    visited = [[False]*m for _ in range(n)]
    visited[x][y] = True
    cnt = 0
    dfs(x, y, [(x, y)], visited)
    print(cnt)