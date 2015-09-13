# Remove Duplicates From Sorted List 2
"""
Given a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list.

For example,
Given 1->2->3->3->4->4->5, return 1->2->5.
Given 1->1->1->2->3, return 2->3.
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

        current = head.next
        prev = head
        duplicate = False
        dummy = unique = ListNode(0)

        while current:
            if current.val != prev.val:  # Transition
                if not duplicate:
                    unique.next = ListNode(prev.val)
                    unique = unique.next
                duplicate = False
            else:
                duplicate = True
            current, prev = current.next, prev.next

        if not duplicate:
            unique.next = ListNode(prev.val)
            unique.next.next = None
        return dummy.next
