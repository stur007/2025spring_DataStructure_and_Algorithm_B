n = int(input())
from collections import deque
qs = [deque([]) for i in range(9)]
q_alpha = {'A':deque([]), 'B':deque([]), 'C':deque([]),'D':deque([])}
ans  = []
s = list(input().split())
for i in range(n):
    qs[int(s[i][-1])-1].append(s[i])
for i in range(9):
    print(f'Queue{i+1}:{" ".join(qs[i])}')
    for _ in range(len(qs[i])):
        char = qs[i].popleft()
        q_alpha[char[0]].append(char)
for x in ['A', 'B', 'C', 'D']:
    print(f'Queue{x}:{" ".join(q_alpha[x])}')
    for _ in range(len(q_alpha[x])):
        ans.append(q_alpha[x].popleft())
print(*ans)