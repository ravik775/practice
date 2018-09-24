# Definition for singly-linked list.
'''
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse
order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.
You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example:
Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.
'''
class ListNode:
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        result, head = None, None
        carry = 0

        def _add_to_result(value):
            nonlocal result, head
            newNode = ListNode(value)
            if result:
                result.next, result = newNode, newNode
            else:
                result, head = newNode, newNode

        while l1 and l2:
            carry, digit = divmod(l1.val + l2.val + carry, 10)
            _add_to_result(digit)
            l1, l2 = l1.next, l2.next

        left_over = l1 if l1 else l2

        while left_over:
            carry, digit = divmod(left_over.val + carry, 10)
            _add_to_result(digit)
            left_over = left_over.next

        if carry:
            _add_to_result(carry)

        return head

if __name__ == '__main__':
    sol = Solution()
    a = ListNode(1)
    a.next = ListNode(8)
    b = ListNode(0)
    sol.addTwoNumbers(a, b)