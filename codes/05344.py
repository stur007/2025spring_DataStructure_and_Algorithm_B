n, k = map(int, input().split())
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
root = Node(0)
node = root
for i in range(1, n+1):
    node.next = Node(i)
    node = node.next
node.next = root.next
ans = []
while True:
    for i in range(k-1):
        root = root.next
    ans.append(root.next.val)
    root.next = root.next.next
    if root.next == root:
        break
print(*ans)
