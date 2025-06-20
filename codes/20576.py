precedence = {'not': 3, 'and': 2, 'or': 1}
class Node:
    def __init__(self, val):
        self.val= val
        self.left = None
        self.right = None

    def __le__(self, other):
        return precedence[self.val] <= precedence[other.val]

    def __lt__(self, other):
        return precedence[self.val] < precedence[other.val]


s = list(input().split())
def parse_tree(s):
    operands = {'False', 'True'}
    operators_stack = []
    operands_stack = []
    for i in range(len(s)):
        if s[i] in operands:
            operands_stack.append(Node(s[i]))
        elif s[i] in precedence:
            node = Node(s[i])
            if operators_stack and operators_stack[-1] != '(' and node <= operators_stack[-1]:
                if operators_stack[-1].val == 'not':
                    operators_stack[-1].right = operands_stack.pop()
                    operands_stack.append(operators_stack.pop())
                else:
                    operators_stack[-1].right = operands_stack.pop()
                    operators_stack[-1].left = operands_stack.pop()
                    operands_stack.append(operators_stack.pop())
            operators_stack.append(node)
        elif s[i] == '(':
            operators_stack.append(s[i])
        else:
            while operators_stack[-1] != '(':
                if operators_stack[-1].val == 'not':
                    operators_stack[-1].right = operands_stack.pop()
                    operands_stack.append(operators_stack.pop())
                else:
                    operators_stack[-1].right = operands_stack.pop()
                    operators_stack[-1].left = operands_stack.pop()
                    operands_stack.append(operators_stack.pop())
            operators_stack.pop()
    while operators_stack:
            if operators_stack[-1].val == 'not':
                operators_stack[-1].right = operands_stack.pop()
                operands_stack.append(operators_stack.pop())
            else:
                operators_stack[-1].right = operands_stack.pop()
                operators_stack[-1].left = operands_stack.pop()
                operands_stack.append(operators_stack.pop())
    return operands_stack.pop()

def inorder(node):
    res = []
    if not node:
        return res
    if node.left and node.left.val in precedence and node.left < node:
        res.extend(['(']+inorder(node.left)+[')']+[node.val])
    else:
        res.extend(inorder(node.left)+[node.val])
    if node.right and node.right.val in precedence and node.right <= node:
        res.extend(['(']+inorder(node.right)+[')'])
    else:
        res.extend(inorder(node.right))
    return res
root = parse_tree(s)
print(*inorder(root))