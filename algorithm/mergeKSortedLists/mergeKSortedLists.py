# Merge k Sorted Lists
"""
Merge k sorted linked lists and return it as one sorted list.
Analyze and describe its complexity.
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    # @param {ListNode[]} lists
    # @return {ListNode}
    def mergeKLists(self, lists):
    	if not lists: return 
    	n = len(lists)

    	while n>1:
    		k = (n+1)/2
    		for i in range(0, n/2):
    			lists[i] = self.mergeTwoLists(lists[i], lists[i+k])
    			n = k
    	return lists[0]

    def mergeTwoLists(self, l1, l2):
        dummy = head = ListNode(0)
        if not l1: return l2
        if not l2: return l1

        while l1 and l2:
            if l1.val>l2.val:
                dummy.next = l2
                l2=l2.next
            else:
                dummy.next = l1
                l1=l1.next
            dummy = dummy.next
        if l1: dummy.next = l1
        if l2: dummy.next = l2
        return head.next