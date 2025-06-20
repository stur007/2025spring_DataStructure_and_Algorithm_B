from collections import deque
a, b, c= map(int, input().split())
def bfs():
    q = deque([(0, 0, 0, '')])
    inQueue = {(0, 0)}
    while q:
        x, y, step, path = q.popleft()
        if x == c or y == c:
            return str(step)+str(path)
        for (nx, ny,npath) in [(a, y, '\nFILL(1)'), (x, b, '\nFILL(2)'), (0, y, '\nDROP(1)'), (x, 0, '\nDROP(2)'), (a, y-a+x, '\nPOUR(2,1)') if y >= a-x else (x+y, 0,'\nPOUR(2,1)'), (x-b+y, b, '\nPOUR(1,2)') if x >= b-y else (0, x+y,'\nPOUR(1,2)')]:
            if (nx, ny) not in inQueue:
                q.append((nx, ny, step+1, path+npath))
                inQueue.add((nx, ny)) # 标记已经访问过的节点
    return 'impossible'

print(bfs())
# 这个题目感觉没有什么难度，应该很好过