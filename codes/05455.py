from collections import deque

s = list(map(int, input().split()))
s = list(dict.fromkeys(s))
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    def __lt__(self, other):
        return  self.val < other.val

def parse_tree(root, node):
    if node < root:
        if root.left:
            parse_tree(root.left, node)
        else:
            root.left = node
    else:
        if root.right:
            parse_tree(root.right, node)
        else:
            root.right = node

def levelorder(root):
    q = deque([root])
    ans = []
    while q:
        node = q.popleft()
        if node:
            ans.append(node.val)
            q.append(node.left)
            q.append(node.right)
    return ans

root = Node(s[0])
for i in range(1, len(s)):
    node = Node(s[i])
    parse_tree(root, node)
print(*levelorder(root))