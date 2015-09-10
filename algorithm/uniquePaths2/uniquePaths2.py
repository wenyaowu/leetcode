# Unique Paths 2
"""
Follow up for "Unique Paths":

Now consider if some obstacles are added to the grids. How many unique paths would there be?

An obstacle and empty space is marked as 1 and 0 respectively in the grid.

For example,
There is one obstacle in the middle of a 3x3 grid as illustrated below.

[
  [0,0,0],
  [0,1,0],
  [0,0,0]
]
The total number of unique paths is 2.

Note: m and n will be at most 100.
"""
class Solution:
    # @param {integer[][]} obstacleGrid
    # @return {integer}
    def uniquePathsWithObstacles(self, obstacleGrid):
    	if not obstacleGrid: return 
    	if obstacleGrid[0][0]: return 0
    	m,n = len(obstacleGrid), len(obstacleGrid[0])
    	dp = [[0 for x in range(n)] for x in range(m)]

    	for i in range(m):
    		if obstacleGrid[i][0]: 
    			dp[i][0] = 0
    			break
    		else: 
    			dp[i][0] = 1
    	for i in range(n):
    		if obstacleGrid[0][i]:
    			dp[0][i] = 0
    			break
    		else:
    			dp[0][i] = 1

    	for i in range(1,m):
    		for j in range(1,n):
    			if obstacleGrid[i][j]:
    				dp[i][j] = 0
    			else:
    				dp[i][j] = dp[i-1][j]+dp[i][j-1]
    	return dp[m-1][n-1]
