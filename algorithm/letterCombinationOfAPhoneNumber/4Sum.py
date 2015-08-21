# 4 Sum
"""
Given an array S of n integers, are there elements
a, b, c, and d in S such that a + b + c + d = target?
Find all unique quadruplets in the array which gives the sum of target.

Note:
Elements in a quadruplet (a,b,c,d) must be in non-descending order. (ie, a ≤ b ≤ c ≤ d)
The solution set must not contain duplicate quadruplets.
    For example, given array S = {1 0 -1 0 -2 2}, and target = 0.

    A solution set is:
    (-1,  0, 0, 1)
    (-2, -1, 1, 2)
    (-2,  0, 0, 2)

"""
class Solution:
    # @param {integer[]} nums
    # @param {integer} target
    # @return {integer[][]}
    def fourSum(self, nums, target):
    	res = []
    	if not nums: return res
    	nums = sorted(nums)
    	for i in range(len(nums)-3):
    		for j in range(i+1,len(nums)-2):
    			head = j+1
    			tail = len(nums)-1
    			while head<tail:
    				temp = nums[i]+nums[j]+nums[head]+nums[tail]
    				if temp==target: 
    					if [nums[i],nums[j],nums[head],nums[tail]] not in res:
    						res.append([nums[i],nums[j],nums[head],nums[tail]])
    					head+=1
    					tail-=1

    				if temp>target: tail-=1
    				if temp<target: head+=1
    	return res
