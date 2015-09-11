# Subsets
"""
Given a set of distinct integers, nums, return all possible subsets.

Note:
Elements in a subset must be in non-descending order.
The solution set must not contain duplicate subsets.
For example,
If nums = [1,2,3], a solution is:

[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]

[[]]-> [[],[1]]-> [[],[1],[2],[1,2]]-> [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
"""
class Solution:
    # @param {integer[]} nums
    # @return {integer[][]}
    def subsets(self, nums):
    	nums = sorted(nums, reverse=True)
    	return self.helper(nums) 
    def helper(self, nums):
    	if not nums:
    		return [[]]
    	res = []
    	current = nums[0]
    	subsets = self.helper(nums[1:])
    	for s in subsets:
    		res.append(s)
    		res.append(s+[current])
    	return res
