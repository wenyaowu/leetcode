# Merge Two Sorted Lists
"""
Merge two sorted linked lists and return it as a new list.
The new list should be made by splicing together the nodes of the first two lists.
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param {ListNode} l1
    # @param {ListNode} l2
    # @return {ListNode}
    def mergeTwoLists(self, l1, l2):
        dummy = head = ListNode(0)
        if not l1: return l2
        if not l2: return l1

        while l1 and l2:
            if l1.val>l2.val:
                dummy.next = l2
                l2=l2.next
                dummy = dummy.next
            else:
                dummy.next = l1
                l1=l1.next
                dummy = dummy.next
        if l1: dummy.next = l1
        if l2: dummy.next = l2
        return head.next