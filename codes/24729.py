class Node:
    def __init__(self, value):
        self.value = value
        self.children = []

def generate_tree(s):
    stack = []
    for char in s:
        if char.isalpha():
            node = Node(char)
            if stack:
                stack[-1].children.append(node)
        elif char == '(':
            stack.append(node)
        elif char == ')':
            node = stack.pop()
    return node
# 自己写代码对class的理解有了一定的深入！

preorder = []
def generate_preorder(node):
    global preorder
    preorder.append(node.value)
    for child in node.children:
        generate_preorder(child)

postorder = []
def generate_postorder(node):
    global postorder
    for child in node.children:
        generate_postorder(child)
    postorder.append(node.value)

s = input()
root = generate_tree(s)
generate_preorder(root)
generate_postorder(root)
print(*preorder, sep = '')
print(*postorder, sep = '')