# Swap Nodes in Pairs
"""
Given a linked list, swap every two adjacent nodes and return its head.

For example,
Given 1->2->3->4, you should return the list as 2->1->4->3.

Your algorithm should use only constant space.
You may not modify the values in the list, only nodes itself can be changed.
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    # @param {ListNode} head
    # @return {ListNode}
	def swapPairs(self, head):
		if not head or not head.next:
			return head
		newHead = head.next
		nextPair = head.next.next
		newHead.next = head
		head.next = self.swapPairs(nextPair)
		return newHead