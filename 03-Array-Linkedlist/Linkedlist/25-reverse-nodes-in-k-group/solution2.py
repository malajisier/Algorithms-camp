# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# 压栈法：题目要求空间复杂度为常数，（不同的测试k之为变量）可能不符合要求

class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        dummy = ListNode(0)
        p = dummy

        while True:
            count = k
            stack = []
            tmp = head

            while count and tmp:
                stack.append(tmp)
                tmp = tmp.next
                count -= 1
            
            # tmp = k+1，count=0完成压栈, tmp=null说明 k > 链表长度
            if count:
                p.next = head
                break
            
            while stack:
                p.next = stack.pop()
                p = p.next
            
            # p.next = tmp
            head = tmp

        return dummy.next