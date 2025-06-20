import sys
sys.setrecursionlimit(1<<30)

def find_parent(x):
    if parent[x] != x:
        parent[x] = find_parent(parent[x])
    return parent[x]

def union(a, b):
    p_a = find_parent(a)
    p_b = find_parent(b)
    if p_a != p_b:
        parent[p_a]= p_b

while True:
    n, m = map(int, input().split())
    if n == m == 0:
        break
    parent = [i for i in range(n)]
    for _ in range(m):
        s = list(map(int, input().split()))
        k = s.pop(0)
        for i in range(1, k):
            union(s[0], s[i])

    suspect = find_parent(0)
    cnt = 0
    for i in range(n):
        if find_parent(parent[i]) == suspect:
            cnt += 1
    print(cnt)