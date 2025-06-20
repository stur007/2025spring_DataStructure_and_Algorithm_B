# 题目要求取值相同的node代表同一节点，用字典把节点记载下来！
class Node:
    def __init__(self, value):
        self.value = value
        self.children = []

def traverse_tree(root, ans):
    for child in root.children:
        if child == root.value:
            ans.append(root.value)
        else:
            traverse_tree(NodeValueDict[child], ans)
    return ans

n = int(input())
NodeValueDict = dict()
NodesValues = set()
ChildrenValues = set()
root = None
for _ in range(n):
    s = list(map(int, input().split()))
    node = Node(s[0])
    NodeValueDict[s[0]] = node
    node.children = sorted(s)
    NodesValues |= set(s)
    if len(s) > 1:
        ChildrenValues |= set(s[1:])

RootValue ,= NodesValues - ChildrenValues
root = NodeValueDict[RootValue]
ans = traverse_tree(root, [])
for i in ans:
    print(i)