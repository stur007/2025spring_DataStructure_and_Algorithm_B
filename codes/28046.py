from collections import deque
import string

class Node:
    def __init__(self):
        self.adjacent = set()

n = int(input())
words = dict()
for _ in range(n):
    s = str(input())
    words[s] = Node()
for word in words:
    if word[0].islower():
        for i in range(4):
            origin_char = word[i]
            for char in list(string.ascii_lowercase):
                if char == origin_char:
                    continue
                if word[:i]+char+word[i+1:] in words:
                    words[word].adjacent.add(word[:i]+char+word[i+1:])
    else:
        for i in range(4):
            origin_char = word[i]
            for char in list(string.ascii_uppercase):
                if char == origin_char:
                    continue
                if word[:i]+char+word[i+1:] in words:
                    words[word].adjacent.add(word[:i]+char+word[i+1:])
# 这个优化确实有点奇怪，但是确实将代码的时间复杂度从O(N^2)降低到了O(25*N)，挺有意思
s, e = input().split()
def bfs():
    if s not in words:
        return 'NO'
    q = deque([s])
    visited = {s:None}
    while q:
        current = q.popleft()
        for neighbor in words[current].adjacent:
            if neighbor not in visited:
                visited[neighbor] = current
                if neighbor == e:
                    path = []
                    node = neighbor
                    while node is not None:
                        path.append(node)
                        node = visited[node]
                    return ' '.join(reversed(path))
                q.append(neighbor)
    return 'NO'
print(bfs())

# 如果使用词桶是不是会更加简化一些呢（时间复杂度降低常数量级）