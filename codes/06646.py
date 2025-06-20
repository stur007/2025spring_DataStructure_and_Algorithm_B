class TreeNode:
    def __init__(self):
        self.left = None
        self.right = None

def depth(node):
    left_depth, right_depth = 1, 1
    if node.left is not None:
        left_depth = depth(node.left)+1
    if node.right is not None:
        right_depth = depth(node.right)+1
    return max(left_depth, right_depth)

n = int(input())
nodes = [TreeNode() for _ in range(n)]
for node in nodes:
    left, right = map(int, input().split())
    if left != -1:
        node.left = nodes[left-1]
    if right != -1:
        node.right = nodes[right-1]

print(depth(nodes[0]))