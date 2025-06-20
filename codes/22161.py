import heapq
class Node:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None
    def __lt__(self, other):
        if self.freq == other.freq:
            return self.char < other.char
        return  self.freq < other.freq

n = int(input())
s = []
for _ in range(n):
    char, freq = input().split()
    heapq.heappush(s, Node(char, int(freq)))
while len(s) > 1:
     node_1 = heapq.heappop(s)
     node_2 = heapq.heappop(s)
     node = Node(min(node_1.char, node_2.char), node_1.freq+node_2.freq)
     node.left = node_1
     node.right = node_2
     heapq.heappush(s, node)
root = s.pop()
encoding = dict()
decoding = dict()
def dfs(node, code):
    if not node.left and not node.right:
        encoding[node.char] = code
        decoding[code] = node.char
        return
    dfs(node.left, code+'0')
    dfs(node.right, code+'1')
dfs(root, '')
while True:
    try:
        s = input()
    except EOFError:
        break
    if s.isalpha():
        ans = ''
        for i in range(len(s)):
            ans += encoding[s[i]]
        print(ans)
    elif s.isdigit():
        ans = ''
        temp = ''
        for i in range(len(s)):
            temp += s[i]
            if temp in decoding:
                ans += decoding[temp]
                temp = ''
        print(ans)

# 第二次写，感觉简单了很多