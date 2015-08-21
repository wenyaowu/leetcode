# Remove Duplicates From Sorted Array
"""
Given a sorted array, remove the duplicates in place such that
each element appear only once and return the new length.

Do not allocate extra space for another array,
you must do this in place with constant memory.

For example,
Given input array nums = [1,1,2],

Your function should return length = 2,
with the first two elements of nums being 1 and 2 respectively.
It doesn't matter what you leave beyond the new length.
"""
class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def removeDuplicates(self,nums):
    	if not nums: return

    	c_p = n_p = 1
    	cur = nums[0]

    	for num in nums[1:]: 
    		if num != cur:
    			nums[n_p] = cur = num
    			n_p += 1
    		c_p += 1
    	return n_p
