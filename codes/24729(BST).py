class Node:
    def __init__(self, val):
        self.val = val
        self.FirstChild = None
        self.NextSibling = None
def parse_tree(s):
    stack = []
    for i in range(len(s)):
        if s[i].isalpha():
            node = Node(s[i])
            if stack:
                if stack[-1] == '(':
                    stack[-2].FirstChild = node
                else:
                    stack[-1].NextSibling = node
            stack.append(node)
        elif s[i] == '(':
            stack.append('(')
        elif s[i] == ')':
            while stack[-1] != '(':
                stack.pop()
            stack.pop()
    return stack.pop()
def preorder(node):
    if node:
        return node.val+preorder(node.FirstChild)+preorder(node.NextSibling)
    return ''
def postorder(node):
    if node:
        return postorder(node.FirstChild)+node.val+postorder(node.NextSibling)
    return ''
s = input()
root = parse_tree(s)
print(preorder(root))
print(postorder(root))