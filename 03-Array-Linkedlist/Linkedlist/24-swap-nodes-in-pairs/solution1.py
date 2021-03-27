# 法一：递归法
# 从头结点开始递归，每次递归都负责交换一对节点，分别用first，second表示
# 每次递归后，返回second，因为它是交换后的新头

# TC:O(n), n: nodes in linked-list
# SC:O(n), n: 递归使用的堆栈空间

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):
    def swapPairs(self, head: ListNode) -> ListNode:
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head

        first, second = head.next, head.next.next

        first.next = self.swapPairs(second.next)
        second.next = first

        return second
