# Combination Sum II
"""
Given a collection of candidate numbers (C) and a target number (T), 
find all unique combinations in C where the candidate numbers sums to T.

Each number in C may only be used once in the combination.

Note:
All numbers (including target) will be positive integers.
Elements in a combination (a1, a2, … , ak) 
must be in non-descending order. (ie, a1 ≤ a2 ≤ … ≤ ak).
The solution set must not contain duplicate combinations.
For example, given candidate set 10,1,2,7,6,1,5 and target 8, 
A solution set is: 
[1, 7] 
[1, 2, 5] 
[2, 6] 
[1, 1, 6] 
"""
class Solution:
    # @param {integer[]} candidates
    # @param {integer} target
    # @return {integer[][]}
    def combinationSum2(self, candidates, target):
        result = []
        candidates.sort()
        for ii, num in enumerate(candidates):
             
            if target>num:
                subsets = self.combinationSum2(candidates[ii+1:], target-num)
                if subsets:
                    for subset in subsets:
                        if [num]+subset not in result:
                            result += [[num]+subset]
            elif target == num:
                if [num] not in result:
                    result += [[num]]
            else:
                break
        return result
