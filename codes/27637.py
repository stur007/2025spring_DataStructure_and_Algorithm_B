class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def parse_tree(s):
    stack = []
    node = None

    for char in s:
        if char.isalpha() or char == '*':
            node = Node(char)
            if stack:
                if stack[-1].left is None:
                    stack[-1].left = node
                else:
                    stack[-1].right = node

        elif char == '(':
            stack.append(node)
        elif char == ')':
            node = stack.pop()

    return node

def preorder(node):
    if (node is None) or (node.val == '*'):
        return ''
    return node.val+preorder(node.left)+preorder(node.right)

def inorder(node):
    if (node is None) or (node.val == '*'):
        return ''
    return inorder(node.left)+node.val+inorder(node.right)

if __name__ == '__main__':
    n = int(input())
    for _ in range(n):
        s = input()
        root = parse_tree(s)
        print(preorder(root))
        print(inorder(root))