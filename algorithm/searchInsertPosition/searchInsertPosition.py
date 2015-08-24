# Search Insert Position
"""
Given a sorted array and a target value, 
return the index if the target is found. 
If not, return the index where it would be if it were inserted in order.

You may assume no duplicates in the array.

Here are few examples.
[1,3,5,6], 5 → 2
[1,3,5,6], 2 → 1
[1,3,5,6], 7 → 4
[1,3,5,6], 0 → 0
"""
class Solution:
    # @param {integer[]} nums
    # @param {integer} target
    # @return {integer}
    def searchInsert(self, nums, target):
    	if not nums: return 0
    	head = 0
    	tail = len(nums)-1
    	while head<tail:
    		mid = (head+tail)/2
    		if nums[mid]<target:
    			head = mid+1
    		else:
    			tail = mid
    	return head+1 if nums[-1]<target else head