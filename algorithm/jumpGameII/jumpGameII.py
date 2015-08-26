# Jump Game II
"""
Given an array of non-negative integers,
you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Your goal is to reach the last index in the minimum number of jumps.

For example:
Given array A = [2,3,1,1,4]

The minimum number of jumps to reach the last index is 2.
(Jump 1 step from index 0 to 1, then 3 steps to the last index.)
"""
class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def jump(self, nums):
        last = 0
        curr = 0
        result = 0
        for i in range(len(nums)):
            if i>last:
                if last == curr:
                    return -1
                last = curr
                result+=1
            curr = max(curr, nums[i]+i)
        return result