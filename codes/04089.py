# 还是用OOP的方案来写比较方便，设函数表达不是很方便
class Node:
    def __init__(self): # 用字典存储值，实现快速搜索
        self.child = {}

class Trie:
    def __init__(self):
        self.root = Node()

    def insert(self, nums):
        curnode = self.root
        for x in nums:
            if x not in curnode.child:
                curnode.child[x] = Node()
            curnode = curnode.child[x]

    def search(self, num):
        curnode = self.root
        for x in num:
            if x not in curnode.child:
                return 0
            curnode = curnode.child[x]
        return 1

t = int(input())
p = []
for _ in range(t):
    n = int(input())
    nums = []
    for _ in range(n):
        nums.append(str(input()))
    nums.sort(reverse = True) # 这个排序还是很重要的，可以减少搜索的次数
    s = 0
    trie = Trie()
    for num in nums:
        s += trie.search(num)
        trie.insert(num)
    if s > 0:
        print('NO')
    else:
        print('YES')
