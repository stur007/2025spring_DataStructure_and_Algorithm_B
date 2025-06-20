t = int(input())
s = list(map(int, input().split()))
s.sort()
def two_pointers():
    left = 0
    right = len(s)-1
    minv = float('inf')
    maxv = float('inf')
    while left < right:
        temp = s[left]+s[right]
        if temp < t:
            left += 1
            minv = min(minv, t- temp)
        elif temp > t:
            right -= 1
            maxv = min(maxv, temp - t)
        else:
            return t
    if maxv < minv:
        return t+maxv
    else:
        return t-minv
print(two_pointers())