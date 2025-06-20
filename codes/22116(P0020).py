class Node:
    def __init__(self, data, next=None):
        self.data, self.next = data, next
class LinkList:  #循环链表
    def __init__(self):
        self.tail = None #链表的尾节点
        self.size = 0 #循环链表的大小
    def isEmpty(self):
        return self.size == 0
    def pushFront(self,data):
        nd = Node(data)
        if self.tail == None: #说明链表为空，没有元素，现在加入一个元素，这个元素肯定是尾节点
            self.tail = nd
            nd.next = self.tail #链表是循环的，尾节点的下一个元素一定是头节点
        else:
            nd.next = self.tail.next
            self.tail.next = nd #在循环链表的头部插入元素
        self.size += 1
    def pushBack(self,data):
        self.pushFront(data)
        self.tail = self.tail.next #在尾部插入元素，相当于在头部插入元素，然后修改尾元素的位置
    def popFront(self): #删除头部元素
        if self.size == 0:
            return None
        else:
            nd = self.tail.next
            self.size -= 1
            if self.size == 0:
                self.tail = None
            else:
                self.tail.next = nd.next
        return nd.data
    def printList(self): #打印列表
        if self.size > 0:
            ptr = self.tail.next
            while True:
                print(ptr.data,end = " ")
                if ptr == self.tail:
                    break
                ptr = ptr.next
            print("")

    def remove(self,data): #删除链表中指定元素
        # 在此处补充你的代码
            if self.size == 0:
                return None

            prev = self.tail
            crnt = self.tail.next

            for _ in range(self.size):
                if crnt.data == data:
                    prev.next = crnt.next
                    self.size -= 1

                    if self.size == 0:
                        self.tail == None
                        # 这是一个挺有意思的问题，如果删除以后是空列表就什么也不返回，但是如果删除之前是空列表就返回None
                    else:
                        if self.tail == crnt:
                            self.tail = prev
                    return True
                prev =prev.next
                crnt=crnt.next

            return False

t = int(input())
for i in range(t):
    lst = list(map(int,input().split()))
    lkList = LinkList()
    for x in lst:
        lkList.pushBack(x)
    lst = list(map(int,input().split()))
    for a in lst:
        result = lkList.remove(a)
        if result == True:
            lkList.printList()
        elif result == False:
            print("NOT FOUND")
        else:
            print("EMPTY")
    print("----------------")