class TreeNode:
    def __init__(self):
        self.left = None
        self.right = None

n = int(input())
nodes = [TreeNode() for _ in range(n)]
have_parent = [False for _ in range(n)]
for node in nodes:
    left, right = map(int, input().split())
    if left != -1:
        node.left = nodes[left]
        have_parent[left] = True
    if right != -1:
        node.right = nodes[right]
        have_parent[right]= True
root = have_parent.index(False)

def depth(node):
    left_depth = depth(node.left)+1 if node.left is not None else 0
    right_depth = depth(node.right)+1 if node.right is not None else 0
    return max(left_depth, right_depth)

def cnt_leaves(nodes):
    cnt = 0
    for node in nodes:
        if node.left is None and node.right is None:
            cnt += 1
    return cnt

print(depth(nodes[root]), cnt_leaves(nodes))