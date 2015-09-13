# Largest Rectangle In Historgram
"""
Given n non-negative integers representing the histogram's bar height where the width of each bar is 1, find the area of largest rectangle in the histogram.


Above is a histogram where width of each bar is 1, given height = [2,1,5,6,2,3].


The largest rectangle is shown in the shaded area, which has area = 10 unit.

For example,
Given height = [2,1,5,6,2,3],
return 10.
"""
class Solution:
    # @param {integer[]} height
    # @return {integer}
    def largestRectangleArea(self, height): 
        if not height: return 0
        max_area = 0
        stack = [0]
        height.append(0)

        for i in range(1,len(height)):
            while stack:
                if height[i]<height[stack[-1]]:
                    h = stack.pop()
                    if stack:
                        max_area = max(max_area, height[h]*(i-stack[-1]-1))
                    else:
                        max_area = max(max_area, height[h]*i)
                else: break
            stack.append(i)
        return max_area
