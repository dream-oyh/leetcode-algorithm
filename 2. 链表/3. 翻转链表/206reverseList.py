# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        first = None
        rear = head
        while rear is not None:
            temp = rear.next
            rear.next = first
            first = rear
            rear = temp
        return first

