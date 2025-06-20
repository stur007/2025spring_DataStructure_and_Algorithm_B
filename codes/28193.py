n, m = map(int, input().split())
father = [i for i in range(n)]
def find_father(x):
    if father[x] != x:
        father[x] = find_father(father[x])
    return father[x]
def union(a, b):
    fa_a = find_father(a)
    fa_b = find_father(b)
    if fa_a != fa_b:
        father[fa_a] = father[b]
c = list(map(int, input().split()))
for _ in range(m):
    x, y = map(int, input().split())
    x -= 1
    y -= 1
    union(x, y)

friends = dict()
for i in range(n):
    fa = find_father(i)
    friends[fa] = min(c[i], friends.get(fa, float('inf')))
print(sum(friends.values()))