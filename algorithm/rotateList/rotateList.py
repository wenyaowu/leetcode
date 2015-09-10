# Rotate List
"""
Given a list, rotate the list to the right by k places, where k is non-negative.

For example:
Given 1->2->3->4->5->NULL and k = 2,
return 4->5->1->2->3->NULL.
"""
class Solution:
    # @param {ListNode} head
    # @param {integer} k
    # @return {ListNode}
    def rotateRight(self, head, k):
    	if not head:
    		return 
    	n = 0  #R Record the length of the list
    	slow = fast = head
    	while fast:
    		n+=1
    		fast = fast.next
    	if k>=n:
    		k%=n
    	# Reset fast
    	fast = head
    	
    	for i in range(k):
    		fast = fast.next

    	while fast.next:
    		fast = fast.next
    		slow = slow.next

    	fast.next = head
    	new_head = slow.next
    	slow.next = None

    	return new_head