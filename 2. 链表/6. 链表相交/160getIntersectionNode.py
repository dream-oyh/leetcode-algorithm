# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        lenA, lenB = 0, 0
        cur = headA
        while cur is not None:
            cur = cur.next
            lenA += 1
        cur = headB
        while cur is not None:
            cur = cur.next
            lenB += 1
        curA, curB = headA, headB
        if lenA > lenB:
            curA, curB = curB, curA
            lenA, lenB = lenB, lenA
        for _ in range(lenB - lenA):
            curB = curB.next
        while curA is not None:
            if curA == curB:
                return curA
            else:
                curA = curA.next
                curB = curB.next
        return None
