n, m = map(int, input().split())
s = list(map(int, input().split()))
for _ in range(m):
    p = input()
    if p[0] == 'C':
        d = int(p[2:])
        for k in range(n):
            s[k] = (s[k]+d)%65536
    elif p[0] == 'Q':
        i = int(p[2:])
        cnt = 0
        for k in range(n):
            if s[k] & (1 << i) :
                cnt += 1
        print(cnt)