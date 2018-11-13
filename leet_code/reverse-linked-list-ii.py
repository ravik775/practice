"""
Reverse a linked list from position m to n. Do it in one-pass.

Note: 1 ≤ m ≤ n ≤ length of list.

Example:

Input: 1->2->3->4->5->NULL, m = 2, n = 4
Output: 1->4->3->2->5->NULL
"""

class Solution:
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        start = ListNode(0)
        start.next = head
        current = start
        prev = None
        
        for p in range(m):
            prev, current = current, current.next
        prev_m = prev
        node_m = None
        node_n = current
        for p in range(m, n+1):
            current.next, node_m, current = node_m, current, current.next
            
        prev_m.next = node_m
        node_n.next = current
        
        return start.next