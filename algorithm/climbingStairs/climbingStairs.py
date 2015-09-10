# Climbing Stairs
"""
You are climbing a stair case. It takes n steps to reach to the top.

Each time you can either climb 1 or 2 steps. 
In how many distinct ways can you climb to the top?
"""
class Solution:
    # @param {integer} n
    # @return {integer}
    def climbStairs(self, n):
    	if n==0 or n==1 or n==2: return n
    	a, b = 1, 2
    	for i in range(n-2):
    		c = a+b
    		a = b
    		b = c
    	return c