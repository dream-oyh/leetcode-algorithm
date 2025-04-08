class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class MyLinkedList(object):

    def __init__(self):
        self.head = ListNode()
        self.size = 0

    def get(self, index):
        """
        :type index: int
        :rtype: int
        """
        if index > self.size - 1 or index < 0:
            return -1
        current = self.move_point_to(index + 1)
        return current.val

    def addAtHead(self, val):
        """
        :type val: int
        :rtype: None
        """
        current = self.head
        new_node = ListNode(val=val)
        new_node.next = current.next
        current.next = new_node
        self.size += 1

    def addAtTail(self, val):
        """
        :type val: int
        :rtype: None
        """
        current = self.move_point_to(self.size)
        new_node = ListNode(val=val)
        current.next = new_node
        self.size += 1

    def addAtIndex(self, index, val):
        """
        :type index: int
        :type val: int
        :rtype: None
        """
        if index < self.size and index >= 0:
            current = self.move_point_to(index)
            new_node = ListNode(val=val)
            new_node.next = current.next
            current.next = new_node
            self.size += 1
        elif index == self.size:
            self.addAtTail(val)
        else:
            return -1

    def deleteAtIndex(self, index):
        """
        :type index: int
        :rtype: None
        """
        if index < (self.size) and index >= 0:
            current = self.move_point_to(index)
            current.next = current.next.next
            self.size -= 1

    def move_point_to(self, index):
        current = self.head
        for _ in range(index):
            current = current.next
        return current


# Your MyLinkedList object will be instantiated and called as such:

obj = MyLinkedList()
obj.addAtHead(2)
obj.deleteAtIndex(1)
obj.addAtHead(2)
obj.addAtHead(7)
obj.addAtHead(3)
obj.addAtHead(2)
obj.addAtHead(5)
obj.addAtTail(5)
print(obj.get(5))
obj.deleteAtIndex(6)
obj.deleteAtIndex(4)