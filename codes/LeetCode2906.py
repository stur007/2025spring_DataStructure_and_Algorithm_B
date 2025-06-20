# 正难则反，既然取余数只能支持乘法运算，那么就使用乘法运算递推
from typing import List
class Solution:
    def constructProductMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        # 在过程中不用除法就能保证结果的正确性！
        n = len(grid)
        m = len(grid[0])
        prev = [1]
        sufv = [1]
        for i in range(n):
            for j in range(m):
                prev.append((prev[-1]*grid[i][j])%12345)
        prev.pop()
        for i in range(n-1, -1, -1):
            for j in range(m-1, -1, -1):
                sufv.append((sufv[-1]*grid[i][j])%12345)
        sufv.pop()
        sufv.reverse()
        q = [[0]*m for _ in range(n)]
        for i in range(n):
            for j in range(m):
                q[i][j] = (prev[i*m+j]*sufv[i*m+j])%12345
        return q