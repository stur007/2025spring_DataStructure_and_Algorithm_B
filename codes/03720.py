class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
def parse_tree():
    """
    读取输入的树形结构（以缩进表示层级），构建对应的二叉树并返回根节点。
    输入格式：
      - 每行一个字符串 s，长度表示节点的层级缩进（即 len(s) - 1），最后一个字符为该节点的值。
      - 当读取到单独的 '0' 时表示该棵树的输入结束。
    """
    stack = []  # 用于存储 (level, node) 元组的栈，便于找到当前节点的父节点
    while True:
        s = input()  # 读取一行输入
        if s == '0':  # 如果读到 '0'，表示当前树的所有节点已输入完毕，退出循环
            break
        # 计算当前行的缩进层级：等于字符串长度减一（最后一个字符是节点值，其余都是前导 '-' 或空格等）
        level = len(s) - 1

        # 构造当前节点，节点的值取字符串的最后一个字符
        node = Node(s[-1])

        if not stack:
            # 如果栈是空的，说明这是第一行输入的节点（即根节点）
            # 把 (root_level, root_node) 压入栈中，供后续节点查找父节点
            stack.append((level, node))
        else:
            # 当前层级 level 与栈顶节点层级比较，查找它的父节点
            # 栈顶元素的层级 >= 当前节点层级，说明栈顶节点不是当前节点的父节点，需要弹出
            while stack and level <= stack[-1][0]:
                stack.pop()
            # 弹出后，新的栈顶就是当前节点的父节点
            parent_node = stack[-1][1]
            # 如果父节点的左子节点为空，就把当前节点插入为左子节点；否则作为右子节点
            if parent_node.left:
                parent_node.right = node
            else:
                parent_node.left = node
            # 将当前节点推入栈，后续读到更深层级的子节点时可以找到它
            stack.append((level, node))

    # parse_tree() 总是返回栈底第一个压入的节点，即根节点
    return stack[0][1]

def preorder(node):
    if not node or node.val == '*':
        return ''
    return node.val + preorder(node.left)+preorder(node.right)
def inorder(node):
    if not node or node.val == '*':
        return ''
    return inorder(node.left)+node.val+inorder(node.right)
def postorder(node):
    if not node or node.val == '*':
        return ''
    return postorder(node.left)+postorder(node.right)+node.val
n = int(input())
for _ in range(n):
    root = parse_tree()
    print(preorder(root))
    print(postorder(root))
    print(inorder(root))
    print()