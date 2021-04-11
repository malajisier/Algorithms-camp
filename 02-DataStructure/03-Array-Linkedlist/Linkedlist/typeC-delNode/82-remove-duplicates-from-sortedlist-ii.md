
### 法一：
```java
class Solution {
    public ListNode deleteDuplicates(ListNode head) {
        ListNode dummy = new ListNode(-1);
        dummy.next = head;
        ListNode cur = dummy;

        while (cur.next != null && cur.next.next != null) {
            if (cur.next.val == cur.next.next.val) {
                ListNode tmp = cur.next;
                while (tmp != null && tmp.next != null && tmp.val == tmp.next.val) {
                    tmp = tmp.next; // tmp 会指向最后一个 相同元素
                }
                cur.next = tmp.next; // cur 初始指向的是dummy
            } else {
                cur = cur.next;
            }
        }

        return dummy.next;
    }
}
```


### 法二：递归实现    
```java
class Solution {
    public ListNode deleteDuplicates(ListNode head) {
        if (head == null || head.next == null) {
            return head;
        }

        if (head.val == head.next.val) {
            while (head != null && head.next != null && head.val == head.next.val) {
                head = head.next;
            }
            // 当前节点是 最后一个相同的节点
            return deleteDuplicates(head.next);
        } else {
            head.next = deleteDuplicates(head.next);
            return head;
        }
    }
}
```