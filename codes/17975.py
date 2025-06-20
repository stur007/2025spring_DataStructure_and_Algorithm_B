import sys

n, m, *rest = map(int, sys.stdin.read().split())
s = rest[:n]
table = [None]*m
ans = []
for value in s:
    key = value%m
    if table[key] == value or table[key] is None:
        table[key] =value
        ans.append(key)
    else:
        i = 1
        signs = [1, -1]
        flag = 1
        while flag:
            for sign in signs:
                temp = (key + sign*i**2)%m
                if table[temp] == value or table[temp] is None:
                    table[temp] = value
                    ans.append(temp)
                    flag = 0
                    break
            i += 1
print(*ans)