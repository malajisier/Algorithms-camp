
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
        while s1 or s2 or carry != 0:
            a = s1.pop() if s1 else 0
            b = s2.pop() if s2 else 0

            s = a + b + carry
            carry =  s // 10
            # 余数 是当前为计算后的结果
            remainder = s % 10

            # 头插法，res作为dummy 再指向新节点
            node = ListNode(remainder)
            node.next = res
            res = node
        return res
```