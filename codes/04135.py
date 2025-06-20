n, m = map(int, input().split())
costs = []
for _ in range(n):
    costs.append(int(input()))

def ok(x):
    temp = 0
    cnt = 0
    for cost in costs:
        if temp + cost <= x:
            temp += cost
        else:
            temp = cost
            cnt += 1
    if temp:
        cnt += 1
    if cnt > m:
        return False
    else:
        return True

def binary_search():
    low = max(costs)
    high = sum(costs)
    while low < high -1:
        mid = (low+high)//2
        if ok(mid):
            high = mid
        else:
            low = mid
    if ok(low):
        return low
    else:
        return high

print(binary_search())