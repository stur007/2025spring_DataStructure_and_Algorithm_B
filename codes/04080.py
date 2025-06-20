import heapq
n = int(input())
s = list(map(int, input().split()))
ans = 0
heapq.heapify(s)
while len(s)>1:
    a= heapq.heappop(s)
    b = heapq.heappop(s)
    ans += a+b
    heapq.heappush(s, a+b)
print(ans)