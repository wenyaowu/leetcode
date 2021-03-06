# Edit Distance
"""
Given two words word1 and word2, find the minimum number of steps required to convert word1 to word2. (each operation is counted as 1 step.)

You have the following 3 operations permitted on a word:

a) Insert a character
b) Delete a character
c) Replace a character
"""
class Solution:
    # @param {string} word1
    # @param {string} word2
    # @return {integer}
    def minDistance(self, word1, word2):
    	m, n = len(word1), len(word2)
    	dp = [[0 for x in range(n+1)] for x in range(m+1)]
    	# Initial condition for dp
    	for i in range(1,m+1):
    		dp[i][0] = i
    	for i in range(1,n+1):
    		dp[0][i] = i

    	# Calculation

    	# Operation criteria
    	"""
    	a) Insert: dp[i][j] = dp[i][j-1]+1
		b) Delete: dp[i][j] = dp[i-1][j]+1
		c) Replace: if w1[i-1]=w2[j-1] dp[i][j] = dp[i-1][j-1], else dp[i][j] = dp[i-1][j-1]+1
    	"""
    	for i in range(1,m+1):
    		for j in range(1,n+1):
    			if word1[i-1]==word2[j-1]:
    				dp[i][j] = min(dp[i][j-1]+1, dp[i-1][j]+1, dp[i-1][j-1])
    			else:
    				dp[i][j] = min(dp[i][j-1]+1, dp[i-1][j]+1, dp[i-1][j-1]+1)
    	return dp[m][n]
