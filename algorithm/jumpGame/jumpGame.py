# Jump Game
"""
Given an array of non-negative integers,
you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Determine if you are able to reach the last index.

For example:
A = [2,3,1,1,4], return true.

A = [3,2,1,0,4], return false.
"""
class Solution:
    # @param {integer[]} nums
    # @return {boolean}
    def canJump(self,nums):
    	if not nums: return False
    	cur = len(nums)-1
    	for i in range(len(nums)-1, -1, -1):
    		if i+nums[i]>=cur: cur=i
    	return cur==0