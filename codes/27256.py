import heapq
from collections import deque, defaultdict

class Heap:
    def __init__(self):
        self.numbers = deque()
        self.greater = []
        self.less = []
        self.greater_size = 0
        self.less_size = 0
        self.to_be_removed = defaultdict(int)

    def pure(self):
        while self.less and self.to_be_removed[-self.less[0]] > 0:
            self.to_be_removed[-heapq.heappop(self.less)] -= 1
        while self.greater and self.to_be_removed[self.greater[0]] > 0:
            self.to_be_removed[heapq.heappop(self.greater)] -= 1
    def balance(self):
        while self.less_size < self.greater_size -1:
            x = heapq.heappop(self.greater)
            if self.to_be_removed[x] > 0:
                self.to_be_removed[x] -= 1
            else:
                self.greater_size -= 1
                self.less_size += 1
                heapq.heappush(self.less, -x)

        while self.less_size > self.greater_size:
            x = -heapq.heappop(self.less)
            if self.to_be_removed[x] > 0:
                self.to_be_removed[x] -= 1
            else:
                self.less_size -= 1
                self.greater_size += 1
                heapq.heappush(self.greater, x)

    def add(self, x):
        self.pure()
        self.numbers.append(x)
        if not self.greater_size:
            self.greater_size += 1
            heapq.heappush(self.greater, x)
        else:
            if x <= self.greater[0]:
                self.less_size += 1
                heapq.heappush(self.less, -x)
            else:
                self.greater_size += 1
                heapq.heappush(self.greater, x)

        self.balance()

    def remove(self):
        self.pure()
        x = self.numbers.popleft()
        self.to_be_removed[x] += 1
        if self.less and x <= -self.less[0]:
            self.less_size -= 1
        else:
            self.greater_size -= 1
        self.balance()

    def mean(self):
        self.pure()
        self.balance()
        if self.less_size < self.greater_size:
            return self.greater[0]
        else:
            x = (self.greater[0] - self.less[0])/2
            if x == int(x):
                return int(x)
            else:
                return x

h = Heap()
n = int(input())
for _ in range(n):
    s = input()
    if 'add' in s:
        h.add(int(s[4:]))
    elif 'del' in s:
        h.remove()
    else:
        print(h.mean())

# 回味一下，感觉其实这道题目不是特别困难，懒删除的方法在之前也应用过，
# 但是判断懒删除的元素在小堆还是大堆中还是有一定思维量的，需要先将堆顶的元素清理干净才能完成。