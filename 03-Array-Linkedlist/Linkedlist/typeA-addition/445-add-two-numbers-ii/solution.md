```python
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        s1, s2 = [], []
        while l1:
            s1.append(l1.val)
            l1 = l1.next
        while l2:
            s2.append(l2.val)
            l2 = l2.next
        
        res = None
        carry = 0
        while s1 or s2 or carry:
            x = 0 if not s1 else s1.pop()
            y = 0 if not s2 else s2.pop()
            s = x + y + carry
            carry = s // 10
            s %= 10
            node = ListNode(s)
            node.next = res
            res = node
        
        return res


```