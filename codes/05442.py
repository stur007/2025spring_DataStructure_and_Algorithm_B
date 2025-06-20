n = int(input())
parent = [i for i in range(n)]
paths = []
def find_parent(x):
    if x != parent[x]:
        parent[x] = find_parent(parent[x])
    return parent[x]

def union(a, b):
    p_a = find_parent(a)
    p_b = find_parent(b)
    if p_a == p_b:
        return False
    parent[p_a] = p_b
    return True

for _ in range(n-1):
    s = list(input().split())
    u = ord(s.pop(0))-65
    m = int(s.pop(0))
    for _ in range(m):
        v = ord(s.pop(0)) -65
        c = int(s.pop(0))
        paths.append((c, u, v))
paths.sort(reverse = True)

ans = 0
for _ in range(len(paths)):
    c, u ,v = paths.pop()
    if union(u, v):
        ans += c
print(ans)