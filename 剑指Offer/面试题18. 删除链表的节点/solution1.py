# 本题与《剑指offer》有一些不同：

# 本题输入的类型为：head: ListNode, val: int
# 剑指offer中，默认输入为 head: ListNode, val: ListNode，即 val 的类型是链表

# 本题解法：使用假头
# TC:O(n), SC:O(1)

class Solution:
    def deleteNode(self, head: ListNode, val: int) -> ListNode:
        dummy = ListNode(0)
        dummy.next = head
        if head.val == val: 
            return head.next 

        while head and head.next:
            if head.next.val == val:   
                head.next = head.next.next
            head = head.next
        return dummy.next


# 输入为整个链表时，对应剑指offer的情况：
# 待删除节点是最后一个时，TC=O(n)，总的平均复杂度O(1), SC:O(1)

# class Solution:
#     def deleteNode(self, head, val):
#         if head is None or val is None:
#             return None
#         if val.next is not None: 
#             tmp = val.next
#             val.val = tmp.val
#             val.next = tmp.next
#         elif head == val: 
#             head = None
#         else:
#             cur = head
#             while cur.next != val:
#                 cur = cur.next
#             cur.next = None
#         return head