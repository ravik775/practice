"""
Given a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list.

Example 1:

Input: 1->2->3->3->4->4->5
Output: 1->2->5
Example 2:

Input: 1->1->1->2->3
Output: 2->3
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head: 
            return head
        
        start = ListNode(0)
        start.next = head
        prev, curr = start, head
        while curr:
            if curr.next and curr.next.val == curr.val:
                # duplicate
                nxt, val = curr.next, curr.val
                while nxt and nxt.val == val:
                    nxt = nxt.next
                curr = nxt
                prev.next = nxt
            else:
                prev, curr = curr, curr.next
        return start.next
                
                
                
        