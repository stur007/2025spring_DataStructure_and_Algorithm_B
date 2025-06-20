class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.father = None

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    nodes = {i:Node(i) for i in range(n)}
    for _ in range(n):
        x, y, z = map(int, input().split())
        if y != -1:
            nodes[x].left = y
            nodes[y].father = x
        if z != -1:
            nodes[x].right = z
            nodes[z].father = x
    for _ in range(m):
        s = input().split()
        if s[0] == '1':
            x = int(s[1])
            y = int(s[2])
            fa_x = nodes[x].father
            fa_y = nodes[y].father
            nodes[x].father, nodes[y].father = fa_y, fa_x
            if nodes[fa_x].left == x and nodes[fa_y].left == y:
                nodes[fa_x].left, nodes[fa_y].left = y, x
            elif nodes[fa_x].left == x and nodes[fa_y].right == y:
                nodes[fa_x].left, nodes[fa_y].right = y, x
            elif nodes[fa_x].right == x and nodes[fa_y].left == y:
                nodes[fa_x].right, nodes[fa_y].left = y, x
            elif nodes[fa_x].right == x and nodes[fa_y].right == y:
                nodes[fa_x].right, nodes[fa_y].right = y, x
        elif s[0] == '2':
            x = int(s[1])
            while nodes[x].left:
                x = nodes[x].left
            print(x)
