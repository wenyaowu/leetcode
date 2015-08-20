# 3Sum
"""
Given an array S of n integers,
are there elements a, b, c in S such that a + b + c = 0?
Find all unique triplets in the array which gives the sum of zero.

Note:
Elements in a triplet (a,b,c) must be in non-descending order. (ie, a ≤ b ≤ c)
The solution set must not contain duplicate triplets.
    For example, given array S = {-1 0 1 2 -1 -4},

    A solution set is:
    (-1, 0, 1)
    (-1, -1, 2)
"""

class Solution:
    # @param {integer[]} nums
    # @return {integer[][]}
    def threeSum(self,nums):
    	res = []
    	if not nums: return res
    	nums = sorted(nums)
    	for i in range(len(nums)):
    		subs = self.twoSum(nums[i+1:], -nums[i])
    		if subs:
    			for sub in subs: 
    				if [nums[i]]+sub not in res:
    					res.append([nums[i]]+sub)
    	return res

    def twoSum(self, nums, target):
    	res = []        
    	num_dict = {}
        for ii, num in enumerate(nums):
            if num not in num_dict:
            	num_dict[target-num]=ii
            else:
            	res.append([nums[num_dict[num]], nums[ii]])
        return res