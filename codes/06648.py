import heapq
t = int(input())
for _ in range(t):
    s = []
    m, n = map(int, input().split())
    for i in range(m):
        s.append(sorted(list(map(int, input().split()))))
    ptr = [0]*m
    ans = [(sum(s[i][ptr[i]]for i in range(m)), ptr[:])]
    visited = {tuple(ptr[:])}
    step = []
    for i in range(m):
        if ptr[i] < n-1:
            leap = s[i][ptr[i]+1]-s[i][ptr[i]]
            heapq.heappush(step, (ans[0][0]+leap, 0, i))
    for i in range(n-1):
        n_ans, idx, ptr_plus= heapq.heappop(step)
        ptr = ans[idx][1][:]
        ptr[ptr_plus] += 1
        while tuple(ptr) in visited:
            n_ans, idx, ptr_plus = heapq.heappop(step)
            ptr = ans[idx][1][:]
            ptr[ptr_plus] += 1
        ans.append((n_ans, ptr[:]))
        visited.add(tuple(ptr))
        for j in range(m):
            if ptr[j] < n-1:
                leap = s[j][ptr[j] + 1] - s[j][ptr[j]]
                heapq.heappush(step, (n_ans+leap, len(ans)-1, j))
    ans_ = list([i[0] for i in ans])
    print(*ans_)