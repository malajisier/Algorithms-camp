迭代实现
- 设置一个哨兵节点 prehead，用于返回排序后的链表
- 维护一个 cur指针，用于往下遍历

```Python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> :
        prehead = ListNode(-1)
        cur = prehead

        while l1 and l2:
            if l1.val <= l2.val:
                cur.next = l1
                l1 = l1.next
            else:
                cur.next = l2
                l2 = l2.next
            cur = cur.next
        
        cur.next = l1 if l1 is not None else l2

        return prehead.next
```

```Java
class Solution {
    public ListNode mergeTwoLists(ListNode l1, ListNode l2) {
        ListNode prehead = new ListNode(-1);
        ListNode cur = prehead;

        while (l1 != null && l2 != null) {
            if (l1.val <= l2.val) {
                cur.next = l1;
                l1 = l1.next;
            } else {
                cur.next = l2;
                l2= l2.next;
            }
            cur = cur.next;
        }
        cur.next = l1 == null ? l2 : l1; 

        return prehead.next;
    }
}
```