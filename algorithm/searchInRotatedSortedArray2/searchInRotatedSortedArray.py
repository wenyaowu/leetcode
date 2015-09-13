# Search In Rotated Sorted Array
"""
Follow up for "Search in Rotated Sorted Array":
What if duplicates are allowed?

Would this affect the run-time complexity? How and why?

Write a function to determine if a given target is in the array.
"""
class Solution:
    # @param {integer[]} nums
    # @param {integer} target
    # @return {boolean}
    def search(self, nums, target):
        head = 0
        tail = len(nums)-1
        
        while head<tail:
            mid = (head+tail)/2
            if nums[mid]==target:
                return True
            if nums[mid]>nums[head]:#left-side is ordered
                if nums[head]<=target<nums[mid]: #search left
                    tail = mid-1
                else: #search right
                    head = mid+1
            elif nums[mid]<nums[head]: #right-side is ordered
                if nums[mid]<target<=nums[tail]: #search right
                    head = mid+1
                else:
                    tail = mid-1
            else:
                head +=1
                
        return True if nums[head]==target else False