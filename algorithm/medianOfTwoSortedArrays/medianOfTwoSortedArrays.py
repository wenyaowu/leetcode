# Median of Two Sorted Arrays
"""
There are two sorted arrays nums1 and nums2
of size m and n respectively.
Find the median of the two sorted arrays.
The overall run time complexity should be O(log (m+n)).
"""

class Solution:
    # @param {integer[]} nums1
    # @param {integer[]} nums2
    # @return {float}
    def findMedianSortedArrays(self, nums1, nums2):
    	m, n = len(nums1), len(nums2)
    	if (m+n)%2 == 0: 
    		return (float(self.findFirstK(nums1, nums2, (m+n)/2))+float(self.findFirstK(nums1, nums2, (m+n)/2+1)))/2
    	else: 
    		return self.findFirstK(nums1, nums2, (m+n)/2+1)


    def findFirstK(self, nums1, nums2, k):
    	# Always set nums1 as the shorter one
    	m, n = len(nums1), len(nums2)
    	if m>n: nums1, nums2 = nums2, nums1
    	if not nums1: return nums2[k-1]

    	if k==1: return min(nums1[0], nums2[0])

    	i1 = min(len(nums1), k/2)
    	i2 = k-i1

    	if nums1[i1-1] > nums2[i2-1]:
    		return self.findFirstK(nums1, nums2[i2:], k-i2)
    	elif nums2[i2-1] > nums1[i1-1]:
    		return self.findFirstK(nums1[i1:], nums2, k-i1)
    	else: return nums1[i1-1]