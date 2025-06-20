n, k = map(int, input().split())
logs = []
for i in range(n):
    logs.append(int(input()))
def is_ok(a):
    cnt = 0
    for log in logs:
        cnt += log//a
    return cnt >= k
def binary_search():
    low = 1
    high = max(logs)
    while low <= high:
        mid = (low+high)//2
        if is_ok(mid):
            low = mid+1
        else:
            high = mid-1
    return high
print(binary_search())