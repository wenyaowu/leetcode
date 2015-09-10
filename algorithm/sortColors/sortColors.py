# Sort Colors
"""
Given an array with n objects colored red, white or blue,
sort them so that objects of the same color are adjacent,
with the colors in the order red, white and blue.

Here, we will use the integers 0, 1, and 2 to represent the color red, white,
and blue respectively.

Note:
You are not suppose to use the library's sort function for this problem.
"""
class Solution:
    # @param {integer[]} nums
    # @return {void} Do not return anything, modify nums in-place instead.
    def sortColors(self, nums):
    	current = 0
    	zero_end = 0
    	two_head = len(nums)-1

    	while current<=two_head:
    		if nums[current] == 0:
    			nums[current], nums[zero_end] = nums[zero_end], nums[current]
    			zero _end +=1
    			current +=1
    		elif nums[current] == 2:
    			nums[current], nums[two_head] = nums[two_head], nums[current]
    			two_head-=1
    		else:
    			current +=1
