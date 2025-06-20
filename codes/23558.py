n, m, L = map(int, input().split())
class Node:
    def __init__(self):
        self.adjacent = list()
nodes = [Node() for _ in range(n)]
for _ in range(m):
    a, b = map(int, input().split())
    nodes[a].adjacent.append(b)
    nodes[b].adjacent.append(a)
root = int(input())
visited = set()
ans = []
def dfs(node, step):
    if step <= L:
        visited.add(node)
        ans.append(node)

        for neighbor in sorted(nodes[node].adjacent):
            if neighbor not in visited:
                dfs(neighbor, step + 1)
dfs(root, 0)
print(*ans)

# 感觉比580C简单