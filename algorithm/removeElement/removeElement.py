# Remove Element
"""
Given an array and a value, remove all instances of that value in place and return the new length.

The order of elements can be changed. It doesn't matter what you leave beyond the new length.
"""
class Solution:
    # @param {integer[]} nums
    # @param {integer} val
    # @return {integer}
    def removeElement(self, nums, val):
        if not nums:
            return 0
        final_length = 0
        for num in nums:
            if num!=val:
                nums[final_length] = num
                final_length+=1
        return final_length