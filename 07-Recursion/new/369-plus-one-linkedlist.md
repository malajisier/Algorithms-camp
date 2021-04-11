### 法一：递归实现      

```java
// bili: guoguo

class Solution {
    // 全局变量：进位标志，每层的递归可以获得上层处理后的信息，来决定是否加一
    int carryBit = 0;

    public ListNode plusOne(ListNode head) {
        head = helper(head);

        if (carryBit == 1) {
            ListNode dummy = new ListNode(1);
            dummy.next = head;
            return dummy;
        } else {
            return head;
        }
    }

    private ListNode helper(ListNode head) {
        // 递归出口
        if (head == null) 
            return null;
        if (head.next == null) {
            head.val += 1;
            if (head.val >= 10) {
                carryBit = 1;
                head.val -= 10;
            }
            return head;
        }
        head.next = helper(head.next);

        // 当前层的处理逻辑
        if (carryBit == 1) {
            head.val += carryBit;
            carryBit = 0;
        } 
        if (carryBit >= 10) {
            head.val -= 10;
            carryBit = 0;
        }

        return head;
    }
}
```

### 法二：官解，找到 最右侧第一个不是9 的节点       
- 该节点的数值加 1    
- 将该节点之后所有节点数值改为 0    

```java
class Solution {
    public ListNode plusOne(ListNode head) {
        ListNode dummy = new ListNode(0);
        dummy.next = head;
        ListNode notNine = dummy;

        while (head != null) {
            if (head.val != 9)
                notNine = head;
            head = head.next;
        }

        notNine.val++;
        notNine = notNine.next;
        while (notNine != null) {
            notNine.val = 0;
            notNine = notNine.next;
        }

        return dummy.val != 0 ? dummy : dummy.next;
    }
}
```