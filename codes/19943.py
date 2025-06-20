n, m = map(int, input().split())
D = [[0]*n for _ in range(n)]
A = [[0]*n for _ in range(n)]
L = [[0]*n for _ in range(n)]
for _ in range(m):
    a, b = map(int, input().split())
    D[a][a] += 1
    D[b][b] += 1
    A[a][b] += 1
    A[b][a] += 1
for i in range(n):
    for j in range(n):
        L[i][j] = D[i][j] - A[i][j]

for r in L:
    print(*r, sep = ' ')
