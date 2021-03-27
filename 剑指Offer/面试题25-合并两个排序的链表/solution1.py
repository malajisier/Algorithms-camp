class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        # 引入伪头节点，方便后续节点的插入
        cur = dummy = ListNode(0)

        # 依次合并l1,l2
        while l1 and l2:
            if l1.val < l2.val:
                cur.next, l1 = l1, l1.next
            else:
                cur.next, l2 = l2, l2.next
            cur = cur.next
        
        # 把剩余的链表，依次插入到末尾
        cur.next = l1 if l1 else l2 
        return dummy.next