# Remove Duplicates From Sorted List
"""
Given a sorted linked list, delete all duplicates such that each element appear only once.

For example,
Given 1->1->2, return 1->2.
Given 1->1->2->3->3, return 1->2->3.
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param {ListNode} head
    # @return {ListNode}
    def deleteDuplicates(self, head):
    	if not head: return None
    	unique = head
    	current = head.next 
    	while current:
    		if current.val != unique.val:
    			unique.next = current
    			unique = unique.next
    		current = current.next
    	unique.next = None
    	return head
