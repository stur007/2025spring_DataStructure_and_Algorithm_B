from collections import deque
while True:
    m, n = map(int ,input().split())
    if m == n == 0:
        break
    maze = []
    orientations = {'east':(0, 1), 'west':(0, -1), 'south':(1, 0), 'north':(-1, 0)}
    positions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    for _ in range(m):
        maze.append(list(map(int, input().split())))
    b1, b2, e1, e2, orientation = input().split()
    orientation = orientations[orientation]
    b1 = int(b1)
    b2 = int(b2)
    e1 = int(e1)
    e2 = int(e2)
    def scope(x, y):
        return 0< x <m and 0< y<n
    def check_obstacles(k, x, y, pos):
        for i in range(min(x, x+k*pos[0])-1, max(x, x+k*pos[0])+1):
            for j in range(min(y, y+k*pos[1])-1, max(y, y+k*pos[1])+1):
                if maze[i][j] == 1:
                    return False
        return True
    def bfs():
        q = deque([(b1, b2, orientation, 0)])
        visited = {(b1,b2, orientation)}
        while q:
            x, y, pos, step = q.popleft()
            if (x, y) == (e1, e2):
                return step
            for k in range(1, 4):
                nx = x+k*pos[0]
                ny = y+k*pos[1]
                if scope(nx, ny) and check_obstacles(k, x, y, pos) and (nx, ny, pos) not in visited:
                    q.append((nx, ny, pos, step+1))
                    visited.add((nx, ny, pos))
            index = positions.index(pos)
            left_pos = positions[(index-1)%4]
            right_pos = positions[(index+1)%4]
            if (x, y, left_pos) not in visited:
                q.append((x, y, left_pos, step+1))
                visited.add((x, y, left_pos))
            if (x, y, right_pos) not in visited:
                q.append((x, y, right_pos, step+1))
                visited.add((x, y, right_pos))
        return -1
    print(bfs())