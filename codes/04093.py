from collections import defaultdict

n = int(input())
ref = dict()
for i in range(n):
    s = list(map(int, input().split()))
    ref[i] = set(s[1:])
m = int(input())
for _ in range(m):
    k = list(map(int, input().split()))
    ref_k = defaultdict(list)
    for i in range(n):
        if k[i] == 1:
            ref_k[1].append(i)
        elif k[i] == -1:
            ref_k[-1].append(i)
    ans = ref[ref_k[1][0]].copy() if ref_k[1] else set() # 似乎是浅拷贝的问题，当然最好能使用内置函数实现
    for i in ref_k[1][1:]:
        ans = ans & ref[i]
    for i in ref_k[-1]:
        ans -= ref[i]
    if ans:
        print(*sorted(list(ans)), sep = ' ')
    else:
        print('NOT FOUND')