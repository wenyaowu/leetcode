# Spiral Matrix 2
"""
Given an integer n, generate a square matrix filled with elements
from 1 to n2 in spiral order.

For example,
Given n = 3,

You should return the following matrix:
[
 [ 1, 2, 3 ],
 [ 8, 9, 4 ],
 [ 7, 6, 5 ]
]
"""
class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        res = [[0 for x in range(n)] for x in range(n)]
        d = 0
        i = j = 0
        cur = 1
        while cur <= n*n:
            if d == 0:
                res[i][j] = cur
                cur+=1
                j+=1
                if j>=n or res[i][j]!=0:
                    j-=1
                    i+=1
                    d = 1
            elif d == 1:
                res[i][j] = cur
                cur+=1
                i+=1
                if i>=n or res[i][j]!=0:
                    i-=1
                    j-=1
                    d = 2
            elif d == 2:
                res[i][j] = cur
                cur+=1
                j-=1
                if j<0 or res[i][j]!=0:
                    j+=1
                    i-=1
                    d = 3
            else:
                res[i][j] = cur
                cur+=1
                i-=1
                if i<0 or res[i][j]!=0:
                    i+=1
                    j+=1
                    d = 0
        return res
