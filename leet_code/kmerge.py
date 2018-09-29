# Definition for singly-linked list.
class ListNode:
     def __init__(self, x):
         self.val = x
         self.next = None


class Solution:

    def merge(self, lista, listb):
        if not (lista and listb):
            return lista or listb

        if lista.val < listb.val:
            head, lista = lista, lista.next
        else:
            head, listb = listb, listb.next
        curr = head

        while lista and listb:
            if lista.val < listb.val:
                curr.next, lista = lista, lista.next
            else:
                curr.next, listb = listb, listb.next
            curr = curr.next

        curr.next = lista or listb
        return head


    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """

        head = None
        while lists:
            len_list, index, index_next = len(lists), 0, 1
            temp = []
            while index_next < len_list:
                temp.append(self.merge(lists[index], lists[index_next]))
                index, index_next = index + 2, index_next + 2

            if index < len_list:
                if index:
                    temp.append(lists[index])
                else:
                    head = lists[index]
            lists = temp

        return head

l1 = ListNode(2)
l1.next = ListNode(3)

l2 = ListNode(1)
l2.next = ListNode(5)

l3 = Solution().mergeKLists([l1, l2])
print( l3)