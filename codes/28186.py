from collections import deque

n, m = map(int, input().split())
s = list(map(int ,input().split()))
q =deque([i for i in range(n)])
while len(q) > 1:
    num = q.popleft()
    s[num] -= m
    if s[num] > 0:
        q.append(num)
print(q[0]+1)