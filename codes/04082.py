class Node:
    def __init__(self, val):
        self.val = val
        self.first_child = None
        self.next_sibling = None

def parse_tree(s):
    stack = []
    for char in s:
        node = Node(char[0])
        while stack:
            pre_node = stack[-1]
            if pre_node.next_sibling:
                stack.pop()
            else:
                break
        if stack:
            pre_node = stack[-1]
            if pre_node.first_child:
                pre_node.next_sibling = node
            else:
                pre_node.first_child = node
        if not(node.val == '$' or char[1] == '1'):
            stack.append(node)
    return stack[0]

"""def preorder(node):
    if not node or node.val == '$':
        return ''
    return node.val+preorder(node.first_child)+preorder(node.next_sibling)
"""
n = int(input())
s = list(input().split())
root = parse_tree(s)

def levelorder(s):
    if not s:
        return []
    children = []
    temp = []
    for node in s:
        if node.val != '$':
            temp.append(node.val)
            if node.first_child:
                children.append(node.first_child)
                child = node.first_child
                while child.next_sibling:
                    child = child.next_sibling
                    children.append(child)
    temp.reverse()
    temp.extend(levelorder(children))
    return temp

print(*levelorder([root]))
