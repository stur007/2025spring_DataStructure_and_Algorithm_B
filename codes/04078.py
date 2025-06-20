class Heapq:
    def __init__(self):
        self.heap = []

    def heappush(self, val):
        self.heap.append(val)
        node_index = len(self.heap)-1
        while True:
            if node_index == 0:
                break
            parent_index = (node_index-1)//2
            if self.heap[parent_index] > self.heap[node_index]:
                self.heap[parent_index], self.heap[node_index]= self.heap[node_index], self.heap[parent_index]
                node_index = parent_index
            else:
                break
    def heappop(self):
        val = self.heap[0]
        if len(self.heap) == 1:
            return self.heap.pop()
        self.heap[0] = self.heap.pop()
        node_index = 0
        while True:
            child_index_1 = 2*node_index+1
            child_index_2 = 2*node_index+2
            if child_index_1 >= len(self.heap):
                break
            elif child_index_2 >= len(self.heap):
                if self.heap[child_index_1] < self.heap[node_index]:
                    self.heap[child_index_1], self.heap[node_index] = self.heap[node_index], self.heap[child_index_1]
                break
            else:
                min_val = min(self.heap[node_index], self.heap[child_index_1], self.heap[child_index_2])
                if min_val == self.heap[node_index]:
                    break
                elif min_val == self.heap[child_index_1]:
                    self.heap[node_index], self.heap[child_index_1] = self.heap[child_index_1], self.heap[node_index]
                    node_index = child_index_1
                else:
                    self.heap[node_index], self.heap[child_index_2] = self.heap[child_index_2], self.heap[node_index]
                    node_index = child_index_2
        return val

heapq = Heapq()
n = int(input())
for _ in range(n):
    s = list(map(int, input().split()))
    if s[0] == 1:
        heapq.heappush(s[1])
    else:
        print(heapq.heappop())