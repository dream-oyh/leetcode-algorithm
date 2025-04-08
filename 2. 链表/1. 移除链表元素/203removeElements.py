# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# LeetCode 上的函数输入是直接输入了 ListNode，不需要再做一次链表到列表的转换
# 但是 vsc 里面调试的时候需要手动编写转换函数


class Solution:
    def removeElements(self, head: list, val):
        # 创建虚拟头部节点以简化删除过程
        linked_head = self.list2linkedlist(head)
        self.print_linkedlist(linked_head)
        dummy_node = ListNode(0, linked_head)
        head = dummy_node
        while 1:
            if head.next is None:
                self.print_linkedlist(dummy_node.next)
                return 1
            if head.next.val == val:
                head.next = head.next.next
            else:
                head = head.next

    # def linkedlist2list(self, head: ListNode):
    #     list = []
    #     while 1:
    #         if head is None:
    #             return list
    #         list.append(head.val)
    #         head = head.next

    def list2linkedlist(self, input_list) -> ListNode:
        dummy_node = ListNode()
        head = dummy_node
        for ele in input_list:
            head.next = ListNode(val=ele)
            head = head.next
        return dummy_node.next

    def print_linkedlist(self, head: ListNode):
        print(head.val, end="->")
        if head.next is None:
            print("none")
            return
        self.print_linkedlist(head.next)


so = Solution()
so.removeElements([1, 2, 3, 6, 5, 6, 6, 6], 6)
