class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

# Try to use the thought of recursion, to divide one big problem into two or more small problems,
# rather than find the relation between just two numbers.

"""
def parse_tree(s):
    if not s:
        return None

    root = Node(s[0])
    for i in range(1, len(s)):
        if s[i] > s[0]:
            root.left = parse_tree(s[1:i])
            root.right = parse_tree(s[i:])
            break
    return root
"""

# This function doesn't work well as I think.
# Just think about this situation, the root node only has the left child!

def parse_tree(s):
    if not s:
        return None

    node = Node(s[0])
    idx = len(s)
    for i in range(1, len(s)):
        if s[i] > s[0]:
            idx = i
            break
    node.left = parse_tree(s[1:idx])
    node.right = parse_tree(s[idx:])

    return node

def postorder(node):
    if node is None:
        return []
    return postorder(node.left)+postorder(node.right)+[node.val]

if __name__ == '__main__':
    n = int(input())
    s = list(map(int, input().split()))

    root = parse_tree(s)
    print(*postorder(root), sep = ' ')