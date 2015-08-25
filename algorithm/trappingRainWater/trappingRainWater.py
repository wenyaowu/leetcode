# Trapping Rain Water
"""
Given n non-negative integers representing an elevation
map where the width of each bar is 1,
compute how much water it is able to trap after raining.

For example, 
Given [0,1,0,2,1,0,1,3,2,1,2,1], return 6.

# Find the highest point from the left
# Find the highest point from the right
# MAX = min(left, right)-height[i]
"""
class Solution:
    # @param {integer[]} height
    # @return {integer}
    def trap(self, height):
    	if not height: return 0
    	n = len(height)
    	res = 0
    	#Form left to right
    	left = [0 for x in range(n)]
    	current_MAX = height[0]
    	for i in range(1,n):
    		left[i] = current_MAX
    		if height[i]>current_MAX:
    			current_MAX = height[i]
    	
    	current_MAX = 0
    	for i in range(n-1, -1, -1):
    		temp = min(left[i], current_MAX)
    		if temp-height[i]>0: res+= (temp-height[i])
    		if height[i]>current_MAX: current_MAX = height[i]
    	return res
