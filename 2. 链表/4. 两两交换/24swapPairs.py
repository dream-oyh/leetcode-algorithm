# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def swapPairs(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        first = self.list2linkedlist(head)
        if head is None or head.next is None:
            return head

        pre = head
        current = head.next
        next = head.next.next

        current.next = pre
        pre.next = self.swapPairs(next)

        return current

    def list2linkedlist(self, input_list) -> ListNode:
        dummy_node = ListNode()
        head = dummy_node
        for ele in input_list:
            head.next = ListNode(val=ele)
            head = head.next
        return dummy_node.next


so = Solution()
so.swapPairs([1, 2, 3])
