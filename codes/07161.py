from collections import deque
n = int(input())
class Node:
    def __init__(self,val):
        self.val = val
        self.children = deque()

def postorder(node):
    order = []
    for child in node.children:
        order += (postorder(child))
    order.append(node.val)
    return order
ans = []
nodes = deque([])
for _ in range(n):
    s = (list(input().split()))
    while s:
        degrees, val = int(s.pop()), s.pop()
        node = Node(val)
        if degrees != 0:
            for i in range(degrees):
                node.children.appendleft(nodes.pop())
        nodes.appendleft(node)
    root = nodes.pop()
    ans += postorder(root)
print(*ans)
