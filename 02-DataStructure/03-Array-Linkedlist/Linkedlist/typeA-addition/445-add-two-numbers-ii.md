顺序链表，与2-两数之和正好相反

- 链表需要从低位到高位依次相加，对于逆序处理，首先考虑到栈
- TC: O(max(m,n)),  SC:O(m+n)

```java
class Solution {
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        Stack<Integer> s1 = new Stack<>();
        Stack<Integer> s2 = new Stack<>();

        while (l1 != null) {
            s1.push(l1.val);
            l1 = l1.next;
        }
        while (l2 != null) {
            s2.push(l2.val);
            l2 = l2.next;
        }

        int carry = 0;
        ListNode dummy = new ListNode(-1);
        while (!s1.isEmpty() || !s2.isEmpty() || carry > 0) {
            int val1 = s1.isEmpty() ? 0 : s1.pop();
            int val2 = s2.isEmpty() ? 0 : s2.pop();
            int sum = val1 + val2 + carry;
            carry = sum / 10;    
            // 余数 作为新node
            ListNode node = new ListNode(sum % 10);
            // 头插法
            node.next = dummy.next;
            dummy.next = node;      
        }
        return dummy.next;
    }
}
```

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
