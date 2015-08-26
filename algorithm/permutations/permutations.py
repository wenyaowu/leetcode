# Permutations
"""
Given a collection of numbers, return all possible permutations.

For example,
[1,2,3] have the following permutations:
[1,2,3], [1,3,2], [2,1,3], [2,3,1], [3,1,2], and [3,2,1].

3 -> curr
[1,2] -> subset

subset[0:i]+[curr]+subset[i:]
subset[0:2]+[curr]+subset[2:]
"""
class Solution:
    # @param {integer[]} nums
    # @return {integer[][]}
    def permute(self, nums):
    	if len(nums)<=1: return [nums] 
    	current = nums[0]
    	res = []
    	subsets = self.permute(nums[1:])
    	if subsets:
    		for subset in subsets:
    			for i in range(len(subset)+1):
    				res.append(subset[0:i]+[current]+subset[i:])
    	return res
