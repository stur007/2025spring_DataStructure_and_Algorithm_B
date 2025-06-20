from collections import deque

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def parse_tree():
    s = input()
    stack = []
    for i in range(len(s)):
        node = Node(s[i])
        if s[i].isupper():
            node.right = stack.pop()
            node.left = stack.pop()
        stack.append(node)
    return stack.pop()

def level_order(root):
    q = deque([root])
    ans = []
    while q:
        node = q.popleft()
        ans.append(node.val)
        if node.left:
            q.append(node.left)
        if node.right:
            q.append(node.right)
    ans.reverse()
    return ''.join(ans)

n = int(input())
for _ in range(n):
    root = parse_tree()
    print(level_order(root))