# Unique Binary Search Tree 
"""
Given n, how many structurally unique BST's (binary search trees) that store values 1...n?

For example,
Given n = 3, there are a total of 5 unique BST's.

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3
"""
class Solution:
    # @param {integer} n
    # @return {integer}
    def numTrees(self, n):
    	dp = [0 for x in range(n+1)]
    	dp[0] = dp[1] = 1
    	for i in range(2,n+1):
    		for k in range(i):
    			dp[i]+=dp[k]*dp[i-k-1]

    	return dp[n]