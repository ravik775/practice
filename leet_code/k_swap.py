# Definition for singly-linked list.
'''
Swap element at Kth Position from starting
'''
class ListNode:
     def __init__(self, x):
         self.val = x
         self.next = None


class Solution:
    def kswap(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if k < 2:
            return head

        result = ListNode(0)
        result.next = head
        before_start = result

        while before_start:
            before_end, start = before_start, before_start.next
            end = start
            count = 1
            while end and count < k:
                before_end, end = end, end.next
                count += 1

            print("%s %s" % (end, count))
            if count < k or not end:
                break

            before_start.next, temp = end, end.next
            if before_end == start:
                end.next = start
            else:
                before_end.next = start
                end.next = start.next
            start.next = temp
            before_start = start

        return result.next
