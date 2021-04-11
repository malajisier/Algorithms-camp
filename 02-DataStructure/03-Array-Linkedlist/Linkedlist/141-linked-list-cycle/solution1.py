class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        # 方法一：快慢指针
        fast, slow = head, head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                return True
        return False    