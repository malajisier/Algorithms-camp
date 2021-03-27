递归实现

```Python
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 is  None:
            return l2
        elif l2 is None:
            return l1
        elif:
            l1.next = mergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next = mergeTwoLists(l1, l2.next)
            return l2
```
