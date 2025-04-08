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
        dummy_node = ListNode(0,first)
        current = dummy_node.next
        if current is None:
            return
        elif current.next is not None:
            next = current.next
            dummy_node, next, current = self.swap(dummy_node, current, next)
            while True:
                
                if current.next is not None:
                    prev = current
                    current = current.next
                    if current.next is not None:
                        next = current.next
                        prev, next, current = self.swap(prev, current, next)
                    else:
                        break
                else:
                    break
        return dummy_node.next

    def swap(self, prev, current, next):

        current.next = next.next
        next.next = current
        prev.next = next
        return prev, next, current

    def list2linkedlist(self, input_list) -> ListNode:
        dummy_node = ListNode()
        head = dummy_node
        for ele in input_list:
            head.next = ListNode(val=ele)
            head = head.next
        return dummy_node.next
    
so = Solution()
so.swapPairs([1,2,3])