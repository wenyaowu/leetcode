# Next Permutation
"""
Implement next permutation, which rearranges numbers into the
lexicographically next greater permutation of numbers.

If such arrangement is not possible, it must rearrange it as
the lowest possible order (ie, sorted in ascending order).

The replacement must be in-place, do not allocate extra memory.

Here are some examples. Inputs are in the left-hand column
and its corresponding outputs are in the right-hand column.
1,2,3 → 1,3,2
3,2,1 → 1,2,3
1,1,5 → 1,5,1
"""
class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if not nums: return 
        v_index = len(nums)-2
        while v_index>=0:
        	if nums[v_index]<nums[v_index+1]:
        		break
        	v_index-=1
        
        r_index = len(nums)-1

        if v_index>=0:
            while r_index>0:
                if nums[r_index]>nums[v_index]: break
                r_index-=1
                
        nums[r_index], nums[v_index] = nums[v_index], nums[r_index]

        nums[v_index+1:] = nums[v_index+1:][::-1]