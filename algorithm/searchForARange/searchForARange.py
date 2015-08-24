# Search For a Range
"""
Given a sorted array of integers, 
find the starting and ending position of a given target value.

Your algorithm's runtime complexity must be in the order of O(log n).

If the target is not found in the array, return [-1, -1].

For example,
Given [5, 7, 7, 8, 8, 10] and target value 8,
return [3, 4].
"""
class Solution:
    # @param {integer[]} nums
    # @param {integer} target
    # @return {integer[]}
    def searchRange(self, nums, target):
        start = self.binarySearch(nums, target-0.5)
        if nums[start]!=target:
            return [-1,-1]
        nums.append(0)
        end = self.binarySearch(nums, target+0.5)-1
        return [start,end]

    def binarySearch(self, nums, target):
    	head = 0
    	tail = len(nums)-1
    	while head<tail:
    		mid = (head+tail)/2
    		if nums[mid]<target:
    			head = mid+1
    		else:
    			tail = mid
    	return head