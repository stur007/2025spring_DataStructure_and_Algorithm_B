from collections import deque,defaultdict
a, b = map(int, input().split())
c, d = map(int, input().split())
m = int(input())
others = set(tuple(map(int, input().split()))for _ in range(m))
def bfs():
    q = deque([(a, b, None, None, 0)])
    visited = defaultdict(list)
    ans_step = float('inf')
    while q:
        x, y ,prex ,prey, step = q.popleft()
        visited[(x, y)].append((prex, prey))
        if step < ans_step:
            if x == c and y == d:
                ans_step = step
                continue
            for dx, dy in [(1, 2), (1, -2), (-1, 2), (-1, -2), (2, 1), (2, -1), (-2, 1), (-2, -1)]:
                if (x+dx//2, y+dy//2) not in others:
                    nx = x+dx
                    ny = y+dy
                    if (nx, ny) not in visited and 0<=nx<=10 and 0<=ny<=10:
                        q.append((nx, ny, x, y, step+1))
        elif step == ans_step:
            while q:
                x, y, prex, prey, step = q.popleft()
                visited[(x, y)].append((prex, prey))
        else:
            break
    ans_route = []
    def dfs(x, y, temp):
        if x is not None and y is not None:
            temp.append(f'({x},{y})')
            for px, py in visited[(x, y)]:
                dfs(px, py, temp)
            temp.pop()
        else:
            ans_route.append('-'.join(list(reversed(temp[:]))))
    dfs(c, d, [])
    if len(set((ans_route))) == 1:
        print(ans_route[0])
    else:
        print(len(set(ans_route)))
bfs()
