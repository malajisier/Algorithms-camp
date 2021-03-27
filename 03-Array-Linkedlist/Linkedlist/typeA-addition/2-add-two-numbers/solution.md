

```java
class Solution {
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        ListNode pre = new ListNode(0);
        ListNode cur = pre;
        int carry = 0;

        while (l1 != null || l2 != null) {
            int x = l1 == null ? 0 : l1.val;
            int y = l2 == null ? 0 : l2.val;
            int sum = x + y + carry;
            
            // 进位 要参与下一位的计算
            carry = sum / 10;
            // 余数作为当前位的计算结果
            int remainder = sum % 10;         
            cur.next = new ListNode(remainder);
            cur = cur.next;
            if (l1 != null) l1 = l1.next;
            if (l2 != null) l2 = l2.next;
        }

        // 剩余进位的话，在最前面加一位
        if (carry == 1) {
            cur.next = new ListNode(carry);
        }
        return pre.next;
    }
}
```