# Maximum Subarray
"""
Find the contiguous subarray within an array
(containing at least one number) which has the largest sum.

For example, given the array [−2,1,−3,4,−1,2,1,−5,4],
the contiguous subarray [4,−1,2,1] has the largest sum = 6.
"""
class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def maxSubArray(self, nums):
    	res = [0 for x in range(len(nums))]
    	res[0] = nums[0]
    	for i in range(1, len(nums)):
    		res[i] = max(res[i-1]+nums[i], nums[i])
    	return max(res)
