s = [float(x) for x in input().split()]
s.sort()
i = int(0.4*len(s))
def check(a):
    a = a/1000000000
    return a*s[i]+1.1**(a*s[i]) >= 85
def binary_search():
    low = 0
    high = 1000000000
    while low <= high:
        mid = (low+high)//2
        if check(mid):
            high = mid - 1
        else:
            low = mid + 1

    return low
print(binary_search())