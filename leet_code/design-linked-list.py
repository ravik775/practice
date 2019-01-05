"""
Design your implementation of the linked list. You can choose to use the singly linked list or the doubly linked list. A node in a singly linked list should have two attributes: val and next. val is the value of the current node, and next is a pointer/reference to the next node. If you want to use the doubly linked list, you will need one more attribute prev to indicate the previous node in the linked list. Assume all nodes in the linked list are 0-indexed.

Implement these functions in your linked list class:

get(index) : Get the value of the index-th node in the linked list. If the index is invalid, return -1.
addAtHead(val) : Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
addAtTail(val) : Append a node of value val to the last element of the linked list.
addAtIndex(index, val) : Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
deleteAtIndex(index) : Delete the index-th node in the linked list, if the index is valid.
Example:

MyLinkedList linkedList = new MyLinkedList();
linkedList.addAtHead(1);
linkedList.addAtTail(3);
linkedList.addAtIndex(1, 2);  // linked list becomes 1->2->3
linkedList.get(1);            // returns 2
linkedList.deleteAtIndex(1);  // now the linked list is 1->3
linkedList.get(1);            // returns 3

"""
class Node:
    __slot__ = ('val', 'next', 'prev')
    
    def __init__(self, v, pr=None, nx=None):
        self.val = v;
        self.next = nx;
        self.prev = pr;
        
class MyLinkedList:
    
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head = None
        self.tail = None
        self.count = 0

    def get(self, index):
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        :type index: int
        :rtype: int
        """
        if 0 <= index < self.count:
            cur, item = self.head, 0
            while (item < index):
                cur = cur.next
                item = item + 1
            
            return cur.val
        return -1

    def addAtHead(self, val):
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        :type val: int
        :rtype: void
        """
        self.head = Node(val, nx=self.head)
        self.count += 1
        if self.tail is None:
            self.tail = self.head
        else:
            self.head.next.prev = self.head
        
    def addAtTail(self, val):
        """
        Append a node of value val to the last element of the linked list.
        :type val: int
        :rtype: void
        """
        self.count = self.count + 1
        self.tail = Node(val, pr=self.tail)
        if self.head is None:
            self.head = self.tail
        else:
            self.tail.prev.next = self.tail
        

    def addAtIndex(self, index, val):
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        :type index: int
        :type val: int
        :rtype: void
        """
			
        if 0 <= index <= self.count:
            cur, item = self.head, 0
            node = Node(val)
            self.count = self.count + 1
            while (item < index):
                cur = cur.next
                item = item + 1
            
            if self.head == cur:
                node.next = self.head
                if self.tail is None:
                    self.tail = node
                else:
                    self.head.prev = node
                self.head = node
            elif self.tail == cur:
                node.next = self.tail
                if self.head is None:
                    self.head = node
                else:
                    node.prev = self.tail.prev
                    node.prev.next = node
                    self.tail.prev = node
            elif cur is None:
                self.tail.next = node
                node.prev = self.tail
                self.tail = node
            else:
                node.prev = cur.prev
                node.prev.next = node
                node.next = cur
                cur.prev = node

    def deleteAtIndex(self, index):
        """
        Delete the index-th node in the linked list, if the index is valid.
        :type index: int
        :rtype: void
        """
        if 0 <= index < self.count:
            cur, item = self.head, 0
            self.count = self.count - 1
            
            while (item < index):
                cur = cur.next
                item = item + 1

            if self.head == cur:
                self.head = self.head.next
                if self.head is None:
                    self.tail = None
                else:
                    self.head.prev = None
            elif self.tail == cur:
                self.tail = self.tail.prev
                if self.tail is None:
                    self.head = None
                else:
                    self.tail.next = None
            else:
                cur.prev.next = cur.next
                cur.next.prev = cur.prev


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)