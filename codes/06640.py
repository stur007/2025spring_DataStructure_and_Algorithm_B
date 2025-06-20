# 方法1：
from collections import defaultdict
n = int(input())
ref = defaultdict(list)
for i in range(n):
    s = set(list(input().split())[1:]) # 题目没说，但是应该是有一句话中重复的单词
    for word in s:
        ref[word].append(i+1)
m = int(input())
for _ in range(m):
    word = input()
    if word in ref:
        print(*ref[word], sep = ' ')
    else:
        print('NOT FOUND')

# 方法2：
n = int(input())
ref = dict()
for i in range(n):
    s = set(list(input().split())[1:])
    ref[i] = s
m = int(input())
for _ in range(m):
    word = input()
    ans = []
    for i in range(n):
        if word in ref[i]:
            ans.append(i+1)
    if ans:
        print(*ans, sep = ' ')
    else:
        print('NOT FOUND')