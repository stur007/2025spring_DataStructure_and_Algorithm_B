class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def generate_tree(i):
    if s[i].isalpha():
        node = Node(s[i])
        node.left, i = generate_tree(i+1)
        node.right, i = generate_tree(i+1)  # 结合python中赋值语句的特性，想想看这两句为什么是精髓？（继承下一步递归的位置操作）
        return node, i
    elif s[i] == '.':
        return None, i

def preorder(node):
    if node is None:
        return ''
    return node.val + preorder(node.left)+preorder(node.right)

def inorder(node):
    if node is None:
        return ''
    return inorder(node.left)+node.val+inorder(node.right)

def postorder(node):
    if node is None:
        return ''
    return postorder(node.left)+postorder(node.right)+node.val

s = input()
head, _ = generate_tree(0)
# print(preorder(head))
print(inorder(head))
print(postorder(head))