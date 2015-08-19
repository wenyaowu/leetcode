# Add Two Numbers
"""
You are given two linked lists representing two
non-negative numbers. The digits are stored in reverse
order and each of their nodes contain a single digit.

Add the two numbers and return it as a linked list.

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8

(2->4->3->1)
(5->6)

(7->0->4->1)
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
    def addTwoNumbers(self, l1, l2):
        dummy = head = ListNode(0)
        carry = 0
        while l1 and l2:
        	temp = l1.val + l2.val + carry
        	dummy.next = ListNode(temp % 10)
        	carry = temp / 10

        	dummy, l1, l2 = dummy.next, l1.next, l2.next
        while l1:
        	temp = l1.val + carry
        	dummy.next = ListNode(temp % 10)
        	carry = temp / 10
        	dummy, l1 = dummy.next, l1.next
        while l2:
        	temp = l2.val + carry
        	dummy.next = ListNode(temp % 10)
        	carry = temp / 10
        	dummy, l2 = dummy.next, l2.next
        if carry:
            dummy.next = ListNode(1) 
        return head.next
