# 使用假头和双指针
# 假头可以简化删除head的情况
# 双指针可以避免.Next.Next的写法

class Solution:
    def deleteNode(self, head: ListNode, val: int) -> ListNode:
        dummy = ListNode(0)
        dummy.next = head
        first = dummy
        second = dummy.next
        
        while True:
            if second.val == val:
                # 直接跳过second
                first.next = second.next
                break
            first = first.next
            second = second.next

        return dummy.next

        dummy.next = head
        first = dummy
        sec = dummy.next

        while True:
            if sec.val == val:
                
 