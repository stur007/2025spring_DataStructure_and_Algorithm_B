class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def parse_bst(leaves):
    if not leaves:
        return
    root = Node(leaves[0])
    for leaf in leaves[1:]:
        insert_node(root, leaf)
    return root

def insert_node(root, leaf):
    if leaf < root.val:
        if root.left is None:
            root.left = Node(leaf)
        else:
            insert_node(root.left, leaf)
    else:
        if root.right is None:
            root.right = Node(leaf)
        else:
            insert_node(root.right, leaf)

def preorder(node):
    if not node:
        return ''
    return node.val+preorder(node.left)+preorder(node.right)

leaves = ''
while True:
    s = input()
    if s == '*':
        root = parse_bst(leaves)
        print(preorder(root))
        leaves = ''
    elif s== '$':
        root = parse_bst(leaves)
        print(preorder(root))
        break
    else:
        leaves = s+leaves