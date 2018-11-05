"""
Given a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.

You should preserve the original relative order of the nodes in each of the two partitions.

Example:

Input: head = 1->4->3->2->5->2, x = 3
Output: 1->2->2->4->3->5
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        lt, ge = ListNode(0), ListNode(0)
        elt, ege, current = lt, ge, head
        while current:
            if current.val < x:
                elt.next, elt  = current, current
                elt.next, current = None, current.next
            else:
                ege.next, ege  = current, current
                ege.next, current = None, current.next
        elt.next = ge.next
        return lt.next