# N-Queens II
"""
Follow up for N-Queens problem.

Now, instead outputting board configurations, return the total number of distinct solutions.
"""
class Solution:
    # @param {integer} n
    # @return {string[][]}
    def totalNQueens(self, n):
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