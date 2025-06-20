"""
其实这个题目还是比较简单的，但是注意一下不能写成一种分解方式将两者相乘，这样肯定矛盾了，只能直接讨论最小的乘积因子。
"""
import math
n = int(input())
def decomposition(s, minv):
    ans = 1
    for n in range(minv, int(math.sqrt(s)+1)):
        if s%n == 0:
            ans += decomposition(s//n, n)
    return ans
for i in range(n):
    s = int(input())
    print(decomposition(s, 2))