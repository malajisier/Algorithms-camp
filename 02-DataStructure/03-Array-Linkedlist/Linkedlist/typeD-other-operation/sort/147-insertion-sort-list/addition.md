链表的快排  
法一：只交换值
```java
class Solution {
    public ListNode sortList(ListNode head) {
        quickSort(head, null);
        return head;
    }

    public quickSort(ListNode head, ListNode tail) {
        if (head == null || head.next == null) return head;
        int pivot = head.val;
        ListNode left = head, cur = head.next;

        while (cur != null) {
            if (cur.val < pivot) {
                left = left.next;
                swap(left, cur);
            } 
            cur = cur.next;
        }
        swap(head, left);
        quickSort(head, left);
        quickSort(left.next, tail);
    }
}
```