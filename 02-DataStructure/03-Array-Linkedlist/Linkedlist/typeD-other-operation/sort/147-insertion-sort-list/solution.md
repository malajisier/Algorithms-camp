### 法一：从前往后寻找插入位置
时间复杂度：O(n^2), 
空间：O(1)

```java
public class ListNode {
    int val;
    ListNode next;
    ListNode() {}
    ListNode(int val) {
        this.val = val;
    }
    ListNode(int val, ListNode next) {
        this.val = val;
        this.next = next;
    }
}

class Solution {
    public ListNode insertionSortList(ListNode head) {
        if (head == null || head.next == null) {
            return head;
        }
        ListNode dummy = new ListNode(0);
        dummy.next = head;
        // last 指向已排序链表的末尾，
        ListNode last = head, cur = head.next;

        while (cur != null) {
            if (last.val <= cur.val) {
                last = last.next;
            } else {
                // pre 指向插入位置 的前一个元素
                ListNode pre = dummy;
                // 寻找插入位置
                while (pre.next.val <= cur.val) {
                    pre = pre.next;
                }
                // 插入
                last.next = cur.next;
                cur.next = pre.next;
                pre.next = cur;
            }
            // 重置cur指针 的位置
            cur = last.next;
        }

        return dummy.next;
    }
}

```