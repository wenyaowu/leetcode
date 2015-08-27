#Permutations II
"""
Given a collection of numbers that might contain duplicates, return all possible unique permutations.

For example,
[1,1,2] have the following unique permutations:
[1,1,2], [1,2,1], and [2,1,1].
"""
class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums)<=1: return [nums] 
    	current = nums[0]
    	res = []
    	subsets = self.permuteUnique(nums[1:])
    	if subsets:
    		for subset in subsets:
    			for i in range(len(subset)+1):
    				if subset[0:i]+[current]+subset[i:] not in res:
    					res.append(subset[0:i]+[current]+subset[i:])
    	return res