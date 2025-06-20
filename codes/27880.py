n, m = map(int, input().split())
paths = []
parent = [i for i in range(n)]
def find_parent(x):
    if parent[x] != x:
        parent[x] = find_parent(parent[x])
    return parent[x]

def union(a, b):
    p_a = find_parent(a)
    p_b = find_parent(b)
    if p_a == p_b:
        return False
    parent[p_a] = p_b
    return True

for i in range(m):
    u,v,c =map(int, input().split())
    paths.append((c, u-1,v-1))

paths.sort(reverse = True)
cnt = 0
max_c = 0
while paths:
    c,u,v = paths.pop()
    if union(u, v):
        cnt += 1
        max_c = c
print(cnt, max_c)