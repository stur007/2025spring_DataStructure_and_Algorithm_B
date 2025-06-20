from _collections import deque


class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def parse_tree(inorder, postorder):
    if not postorder or not inorder:
        return None

    root_val = postorder[-1]
    root_idx = inorder.index(root_val)
    left_inorder = inorder[:root_idx]
    right_inorder = inorder[root_idx+1:]
    left_postorder = postorder[:len(left_inorder)]
    right_postorder = postorder[len(left_inorder):-1]
    root = Node(root_val)
    root.left = parse_tree(left_inorder, left_postorder)
    root.right = parse_tree(right_inorder, right_postorder)

    return root

def dfs(root):
    q = deque([root])
    ans = ''
    visited = set()
    while q:
        node = q.popleft()
        if (node is not None):
            ans += node.val
            q.append(node.left)
            q.append(node.right)

    return ans

if __name__ == "__main__":
    n = int(input())
    for _ in range(n):
        a = input()
        b = input()
        inorder = []
        postorder = []
        for char in a:
            inorder.append(char)
        for char in b:
            postorder.append(char)

        root = parse_tree(inorder, postorder)
        print(dfs(root))