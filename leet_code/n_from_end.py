'''
Given a linked list, remove the n-th node from the end of list and return its head.

Example:

Given linked list: 1->2->3->4->5, and n = 2.

After removing the second node from the end, the linked list becomes 1->2->3->5.
Note:

Given n will always be valid.
'''
class Solution:
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """

        if not head: return None  # no values to delete

        n_node_prev = None
        n_node = head
        curr = head
        n = n - 1

        while n:
            curr, n = curr.next, n - 1

        while curr.next:
            curr, n_node_prev, n_node = curr.next, n_node, n_node.next

        if n_node_prev is None:
            return head.next

        n_node_prev.next = n_node.next

        return head
