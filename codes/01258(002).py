import heapq
while True:
    try:
        n = int(input())
    except EOFError:
        break

    edges = []
    for i in range(n):
        s = list(map(int, input().split()))
        for j, edge in enumerate(s):
            heapq.heappush(edges, (edge, i, j))

    father = [i for i in range(n)]
    def find_father(x):
        if father[x] != x:
            father[x] = find_father(father[x])
        return father[x]

    def union(a, b):
        fa_a = find_father(a)
        fa_b = find_father(b)
        if fa_a == fa_b:
            return False
        father[fa_a] = fa_b
        return True

    ans = 0
    while edges:
        edge, i, j = heapq.heappop(edges)
        if union(i, j):
            ans += edge

    print(ans)