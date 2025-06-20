class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

while True:
    try:
        preorder = input()
        inorder = input()
    except EOFError:
        break
    def parse_tree(preorder, inorder):
        if not inorder or not preorder:
            return None
        node = Node(preorder[0])
        index = inorder.index(node.val)
        node.left = parse_tree(preorder[1:index+1], inorder[:index])
        node.right = parse_tree(preorder[index+1:], inorder[index+1:])
        return node
    root = parse_tree(preorder, inorder)
    def postorder(node):
        if not node:
            return ''
        return postorder(node.left)+postorder(node.right)+node.val
    print(postorder(root))