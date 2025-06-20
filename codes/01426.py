# 感觉这个题目还是挺神奇的，将01的数字看作二叉树，对树进行bfs

from collections import deque

def bfs(n):
    q = deque([1])
    visited = {1:None}
    while q:
        x = q.popleft()
        x1 = (10*x)%n
        if x1 not in visited:
            visited[x1] = (x, 0)
            q.append(x1)
        if x1 == 0:
            return visited
        x2 = (10*x+1)%n
        if x2 not in visited:
            visited[x2] = (x, 1)
            q.append(x2)
        if x2 == 0:
            return visited
while True:
    n = int(input())
    if n == 0:
        break
    if n == 1:
        print(1)
    else:
        paths = bfs(n)
        path = []
        x = 0
        while paths[x] is not None:
            path.append(paths[x][1])
            x = paths[x][0]
        path.reverse()
        ans = 1
        for i in path:
            if i == 0:
                ans = 10*ans
            else:
                ans = 10*ans +1
        print(ans)