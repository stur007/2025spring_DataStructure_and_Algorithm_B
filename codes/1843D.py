from collections import defaultdict, deque
"""
CF平台数据量太大，不停地爆栈，太烦人了。
"""
def parse_tree(neighbors):
    nodes = dict()
    nodes[1] = list()
    q =deque([1])
    visited = {1}
    while q:
        root = q.popleft()
        for neighbor in neighbors[root]:
            if neighbor not in visited:
                q.append(neighbor)
                nodes[neighbor] = list()
                nodes[root].append(neighbor)
                visited.add(neighbor)
    return nodes

t = int(input())
for _ in range(t):
    n = int(input())
    neighbors = defaultdict(list)
    for _ in range(n-1):
        u, v = map(int, input().split())
        neighbors[u].append(v)
        neighbors[v].append(u)
    nodes = parse_tree(neighbors)

    q = int(input())
    ans = [0]*(n+1)
    stack = [1]
    order = []

    while stack:
        node = stack.pop()
        order.append(node)

        for child in nodes[node]:
            stack.append(child)
    order.reverse()
    for node in order:
        if not nodes[node]:
            ans[node] = 1
        else:
            ans[node]= sum(ans[child] for child in nodes[node])
    for _ in range(q):
        x, y = map(int, input().split())
        print(ans[x]*ans[y])