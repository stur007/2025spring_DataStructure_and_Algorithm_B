while True:
    try:
        n, m = map(int, input().split())
    except EOFError:
        break
    father = [i for i in range(n)]
    def find_father(x):
        if x != father[x]:
            father[x] = find_father(father[x])
        return father[x]
    def union(a, b):
        father_a =find_father(a)
        father_b = find_father(b)
        if father_a != father_b:
            father[father_b] = father_a
            print('No')
        else:
            print('Yes')
    for _ in range(m):
        a, b = map(int, input().split())
        union(a-1, b-1)
    ans = []
    for i in range(n):
        if father[i] == i:
            ans.append(i+1)
    print(len(ans))
    print(*ans)