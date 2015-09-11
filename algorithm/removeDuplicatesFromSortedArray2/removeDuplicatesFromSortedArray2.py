# Remove Duplicates From Sorted Array 2
"""
Follow up for "Remove Duplicates":
What if duplicates are allowed at most twice?

For example,
Given sorted array nums = [1,1,1,2,2,3],

Your function should return length = 5,
with the first five elements of nums being 1, 1, 2, 2 and 3.
It doesn't matter what you leave beyond the new length.
"""
class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def removeDuplicates(self, nums):
        if not nums:
            return 0
        duplicate = 1
        current_pointer = 1
        current_num = nums[0]
        non_dup = 1
        while current_pointer<len(nums):
            if nums[current_pointer]!=current_num:
                nums[non_dup]=nums[current_pointer]
                current_num = nums[current_pointer]
                non_dup+=1
                duplicate = 1
            else:
                if duplicate<2:
                    nums[non_dup]=nums[current_pointer]
                    duplicate+=1
                    non_dup+=1
            current_pointer+=1
        return non_dup