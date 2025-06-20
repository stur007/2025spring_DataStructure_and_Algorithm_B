class Node:
    def __init__(self):
        self.children = dict()

class Trie:
    def __init__(self):
        self.root = Node()

    def insert_num(self, num):
        current_node = self.root
        for x in num:
            if x not in current_node.children:
                current_node.children[x] = Node()
            current_node = current_node.children[x]
            if 'end' in current_node.children:
                return False
        current_node.children['end']= None
        return True

t = int(input())
for _ in range(t):
    trie = Trie()
    n = int(input())
    nums = []
    for _ in range(n):
        s = input()
        nums.append(s)
    nums.sort()
    for s in nums:
        if not trie.insert_num(s):
            print('NO')
            break
    else:
        print('YES')