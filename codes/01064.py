n, k = map(int, input().split())
s = []
for _ in range(n):
    s.append(int(float(input())*100))

def ok(a):
    ans = 0
    for length in s:
        ans += length//a
    return ans >= k

def binary_search():
    low = 1
    high = max(s)*100 # be careful about this max() or min() function!
    while low + 1 < high:
        mid = (low+high)//2
        if ok(mid):
            low = mid
        else:
            high = mid
    if ok(high):
        return high/100
    elif ok(low):
        return low/100
    else:
        return 0

print(f'{binary_search():.2f}')