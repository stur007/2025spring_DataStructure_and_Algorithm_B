n = int(input())
heap = list(map(int, input().split()))
series = []
def dfs(i, temp):
    temp.append(str(heap[i]))
    if 2*i+2 < n:
        dfs(2*i+2, temp)
    if 2*i+1 < n:
        dfs(2*i+1, temp)
    else:
        series.append(' '.join(temp))
    temp.pop()
dfs(0, [])
for serial in series:
    print(serial)
def maxheap(i):
    flag = True
    if 2*i+1 < n:
        if heap[2*i+1]>heap[i]:
            return False
        flag = flag and maxheap(2*i+1)
    if 2*i+2 < n:
        if heap[2*i+2]>heap[i]:
            return False
        flag = flag and maxheap(2*i+1)
    return flag
def minheap(i):
    flag = True
    if 2*i+1 < n:
        if heap[2*i+1]<heap[i]:
            return False
        flag = flag and minheap(2*i+1)
    if 2*i+2 < n:
        if heap[2*i+2]<heap[i]:
            return False
        flag = flag and minheap(2*i+1)
    return flag

if maxheap(0):
    print('Max Heap')
elif minheap(0):
    print('Min Heap')
else:
    print('Not Heap')