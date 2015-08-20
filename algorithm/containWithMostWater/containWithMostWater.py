# Contain With Most Water
"""
Given n non-negative integers a1, a2, ..., an,
where each represents a point at coordinate (i, ai).
n vertical lines are drawn such that the two endpoints of
line i is at (i, ai) and (i, 0). Find two lines, which
together with x-axis forms a container, such that the
container contains the most water.

"""


class Solution:
    # @param {integer[]} height
    # @return {integer}
    def maxArea(self, height):
    	if not height: return 0
    	head = 0
    	tail = len(height)-1
    	max_v = 0
    	while head<=tail:
    		max_v = max(max_v, min(height[head], height[tail]) * (tail-head))
    		if height[head]<height[tail]:head+=1
    		else:tail-=1
    	return max_v