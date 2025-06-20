father = [i for i in range(26)]
def find_father(x):
    if father[x] != x:
        father[x] = find_father(father[x])
    return father[x]
def union(a, b):
    fa_a = find_father(a)
    fa_b = find_father(b)
    if fa_a != fa_b:
        father[fa_a] = father[b]
def check(a, b):
    fa_a = find_father(a)
    fa_b = find_father(b)
    if fa_a == fa_b:
        return False
    else:
        return True

n = int(input())
check_zone = set()
for _ in range(n):
    s = input()
    x = ord(s[0])-97
    y = ord(s[-1])-97
    if s[1:3] == "==":
        union(x, y)
    else:
        check_zone.add((x, y))
for x, y in check_zone:
    if not check(x, y):
        print('False')
        break
else:
    print('True')
