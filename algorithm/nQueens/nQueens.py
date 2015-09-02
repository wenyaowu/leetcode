# N-Queens
"""
The n-queens puzzle is the problem of placing n queens on an n×n chessboard such that no two queens attack each other.



Given an integer n, return all distinct solutions to the n-queens puzzle.

Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' both indicate a queen and an empty space respectively.

For example,
There exist two distinct solutions to the 4-queens puzzle:

[
 [".Q..",  // Solution 1
  "...Q",
  "Q...",
  "..Q."],

 ["..Q.",  // Solution 2
  "Q...",
  "...Q",
  ".Q.."]
]
"""
class Solution:
    # @param {integer} n
    # @return {string[][]}
    def solveNQueens(self, n):
    	self.res = []
    	self.solveNQueensHelper(n, 0, [])
    	return len(self.res)
    def solveNQueensHelper(self, n, row, cols):
    	if row==n: #Append result
    		temp =  [['.' for x in range(n)] for x in range(n)]
    		for i,c in enumerate(cols):
    			temp[i][c] = 'Q'
    		for i in range(n):
    			temp[i] = ''.join(temp[i])
    		self.res.append(temp)

    	for c in range(n):
    		if self.isValid(row, c, cols):
    			self.solveNQueensHelper(n, row+1, cols+[c])

    def isValid(self, r, c, cols):
    	if len(cols)>r: return False
    	for i,col in enumerate(cols):
    		if c==col: return False
    		if abs(c-col)==abs(r-i): return False
    	return True