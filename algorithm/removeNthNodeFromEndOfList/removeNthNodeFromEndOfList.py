# Remove Nth Node From End of List
"""
Given a linked list, remove the nth node from
the end of list and return its head.

For example,

   Given linked list: 1->2->3->4->5, and n = 2.

   After removing the second node from the end,
   the linked list becomes 1->2->3->5.
Note:
Given n will always be valid.
Try to do this in one pass.
"""


class Solution:
    # @param {ListNode} head
    # @param {integer} n
    # @return {ListNode}
    def removeNthFromEnd(self, head, n):
    	if not head: return 
    	fast = slow = head
    	for i in range(n):
    		fast = fast.next

    	#Edge cases: (1) Head (2) tail
    	if not fast: # head
    		return head.next

    	while fast.next:
    		fast = fast.next
    		slow = slow.next
    	slow.next = slow.next.next

    	return head