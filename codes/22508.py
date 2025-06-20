from collections import deque

class Node:
    def __init__(self):
        self.win_times = 0
        self.winners = []

n, m = map(int, input().split())
nodes = [Node() for _ in range(n)]
for _ in range(m):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    nodes[a].win_times += 1
    nodes[b].winners.append(nodes[a])

q = deque([])
for node in nodes:
    if node.win_times == 0:
        q.append(node)
cnt = 0
ans = 0
while q:
    s = len(q)
    ans += cnt*s
    for _ in range(s):
        node = q.popleft()
        for winner in node.winners:
            winner.win_times -= 1
            if winner.win_times == 0:
                q.append(winner)
    cnt += 1
print(ans+100*n)