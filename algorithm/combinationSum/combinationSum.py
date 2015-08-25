# Combination Sum
"""
Given a set of candidate numbers (C) and a target number (T),
find all unique combinations in C where the candidate numbers sums to T.

The same repeated number may be chosen from C unlimited number of times.

Note:
All numbers (including target) will be positive integers.
Elements in a combination (a1, a2, … , ak) 
must be in non-descending order. (ie, a1 ≤ a2 ≤ … ≤ ak).
The solution set must not contain duplicate combinations.
For example, given candidate set 2,3,6,7 and target 7, 
A solution set is: 
[7] 
[2, 2, 3] 
"""

class Solution:
    # @param {integer[]} candidates
    # @param {integer} target
    # @return {integer[][]}
    def combinationSum(self, candidates, target):
    	candidates = sorted(candidates)
    	self.result = []
    	self.helper([], candidates, target)
    	return self.result
    def helper(self, current, candidates, target):
    	if target<0: return 
    	if target==0:
    		self.result.append(current)
    	for i in range(len(candidates)):
    		self.helper(current+[candidates[i]], candidates[i:], target-candidates[i])
