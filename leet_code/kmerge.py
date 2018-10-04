'''
Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.

Example:

Input:
[
  1->4->5,
  1->3->4,
  2->6
]
Output: 1->1->2->3->4->4->5->6

'''

def print_(x):
 while x:
    print(x.val)
    x = x.next

class Solution:

    def merge(self, lista, listb):
        if lista and listb:
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
            print_(head)
            return head
        return lista or listb

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
