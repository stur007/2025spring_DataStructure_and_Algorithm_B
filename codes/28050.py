"""from collections import deque
n = int(input())
x, y = map(int, input().split())
visited = {(x, y)}
q = deque([(x, y)])
while q:
    x, y = q.popleft()
    for dx, dy in [(1, 2), (1, -2), (-1, 2), (-1, -2),
                   (2, 1), (2, -1), (-2, 1), (-2, -1)]:
        nx = x+dx
        ny = y+dy
        if 0 <= nx<n and 0<= ny < n and (nx, ny) not in visited:
            visited.add((nx, ny))
            q.append((nx, ny))
if len(visited) == n*n:
    print('success')
else:
    print('fail')"""
# 能否有遍历的路径 -> dfs!
# 采用 Warnsdorff’s Rule 进行搜索，优先选择出度最小的下一步路径，从而提高找到完整骑士周游路径的成功率。
import sys

sys.setrecursionlimit(1 << 30)
n = int(input())
a, b = map(int, input().split())
visited = [[False]*n for _ in range(n)]
visited[a][b] = True

def get_degree(x, y):
    cnt = 0
    moves = [(1, 2), (1, -2), (-1, 2), (-1, -2), (2, 1), (2, -1), (-2, 1), (-2, -1)]
    for dx, dy in moves:
        nx = x + dx
        ny = y + dy
        if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
            cnt += 1
    return cnt

def dfs(x, y, temp):
    if temp == n*n:
        return True
    moves = [(1, 2), (1, -2), (-1, 2), (-1, -2),(2, 1), (2, -1), (-2, 1), (-2, -1)]
    n_step = []
    for dx, dy in moves:
        nx = x + dx
        ny = y + dy
        if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
            n_step.append((get_degree(nx, ny), nx, ny))
    n_step.sort()
    for _,nx, ny in n_step:
        visited[nx][ny] = True
        temp += 1
        if dfs(nx, ny, temp):
            return True
        temp -= 1
        visited[nx][ny] = False

if dfs(a, b,1):
    print('success')
else:
    print('fail')