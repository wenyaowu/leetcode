# Combinations
"""
Given two integers n and k, return all possible
combinations of k numbers out of 1 ... n.

For example,
If n = 4 and k = 2, a solution is:

[
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],
]
"""
class Solution:
    # @param {integer} n
    # @param {integer} k
    # @return {integer[][]}
    def combine(self, n, k):
    	return self.helper([x for x in range(1,n+1)], k)
    def helper(self, nums, k):
    	if k == 1:
    		return [[x] for x in nums]
    	res = []
    	for i in range(len(nums)):
    		subsets = self.helper(nums[i+1:], k-1)
    		if subsets:
    			res+=[[nums[i]]+subset for subset in subsets]
    	return res