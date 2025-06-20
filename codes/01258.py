import heapq
while True:
    try:
        n = int(input())
    except EOFError:
        break
    matrix = []
    for _ in range(n):
        matrix.append(list(map(int, input().split())))

    edges = []
    visited = {0}
    ans = 0

    for i, edge in enumerate(matrix[0]):
        heapq.heappush(edges, (edge, i))
    while len(visited) < n:
        edge, node = heapq.heappop(edges)
        if node in visited:
            continue
        ans += edge
        visited.add(node)
        for i, edge in enumerate(matrix[node]):
            heapq.heappush(edges, (edge, i))
    print(ans)