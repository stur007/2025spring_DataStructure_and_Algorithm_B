def find(x, father):
    if father[x] != x:
        father[x] = find(father[x], father)
    return father[x]

def union_set(a, b, father):
    fa_a = find(a, father)
    fa_b = find(b, father)
    if fa_a != fa_b:
        father[fa_a] = fa_b
def init(n):
    return [i for i in range(n)]

t = 0
while True:
    t += 1
    n, m = map(int, input().split())
    if n == m == 0:
        break

    father = init(n)
    for _ in range(m):
        a, b = map(int, input().split())
        union_set(a-1, b-1, father)
    # print(father)
    cnt = sum(1 for i in range(n) if father[i] == i)
    print(f'Case {t}: {cnt}')