class Node:
    def __init__(self, type):
        self.type = type
        self.left = None
        self.right = None
def parse_tree(s):
    if '0' not in s:
        type = 'I'
    elif '1' not in s:
        type = 'B'
    else:
        type = 'F'
    node = Node(type)
    n = len(s)
    if n >1:
        node.left = parse_tree(s[:n//2])
        node.right = parse_tree(s[n//2:])
    return node
def postorder(node):
    if not node:
        return ''
    return postorder(node.left)+postorder(node.right)+node.type
input()
s = input()
root = parse_tree(s)
print(postorder(root))