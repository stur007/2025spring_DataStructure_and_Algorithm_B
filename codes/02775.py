class Node:
    def __init__(self, name):
        self.name = name
        self.files = []
        self.children = []

def print_dir(prev, node):
    for child in node.children:
        print(f'{prev}|     {child.name}')
        print_dir(prev + '|     ', child)
    node.files.sort()
    for file in node.files:
        print(f'{prev}{file}')

def print_file(x):
    print(f'DATA SET {x}:')
    root = stack.pop()
    print('ROOT')
    print_dir('', root)
    print()
x = 1
root = Node('ROOT')
stack = [root]
while True:
    s = input()
    if s == '#':
        break
    elif s == '*':
        print_file(x)
        x += 1
        root = Node('ROOT')
        stack = [root]
    elif s[0] == 'f':
        stack[-1].files.append(s)
    elif s[0] == 'd':
        dir = Node(s)
        stack[-1].children.append(dir)
        stack.append(dir)
    elif s == ']':
        stack.pop()

# 这个题目没有什么难度，就是比较麻烦