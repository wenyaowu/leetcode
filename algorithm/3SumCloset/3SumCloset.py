# 3 Sum Closet
"""
Given an array S of n integers, find three integers
in S such that the sum is closest to a given number,
target. Return the sum of the three integers.
You may assume that each input would have exactly one solution.

    For example, given array S = {-1 2 1 -4}, and target = 1.

    The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).

"""

class Solution:
    # @param {integer[]} nums
    # @param {integer} target
    # @return {integer}
    def threeSumClosest(self, nums, target):
    	nums = sorted(nums)
    	min_gap = pow(2,31)-1
    	for i in range(len(nums)-2):
    		head = i+1
    		tail = len(nums)-1
    		while head < tail:
    			temp = nums[i]+nums[head]+nums[tail]

    			if abs(temp-target)<min_gap:
    				min_gap = abs(temp-target)
    				result = temp

    			if temp < target:
    				head+=1
    			elif temp > target:
    				tail-=1
    			else:
    				return temp
    	return result