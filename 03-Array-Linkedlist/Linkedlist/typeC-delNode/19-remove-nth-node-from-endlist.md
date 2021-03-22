- 进阶要求：一趟扫描实现     


### 法一：快慢指针    
思路：快指针先走 n步，然后快慢指针一起走，快指针走到尾，快慢指针之间就会相差n
TC:O(L), L 为链表长度， SC:O(1)     

```python
# 写法一：
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        slow, fast = head, head
        while fast:
            if n < 0:
                slow = slow.next
            n -= 1
            fast = fast.next
        
        if n == 0: return head.next
        slow.next = slow.next.next
        return head

# 写法二：
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummy = ListNode(0, head)
        first, second = head, dummy

        for i in range(n):
            first = first.next
        
        while first:
            first = first.next
            second = second.next
        
        first.next = first.next.next
        return dummy.next

```
   
   
### 法二：先计算链表长度，再删除节点   
TC:` O(n), SC: O(1)   

```java
class Solution {
    public ListNode removeNthFromEnd(ListNode head, int n) {
        ListNode dummy = new ListNode(0, head);
        int length = getLength(head);
        ListNode cur = dummy;

        // 正数第 l-n+1 个节点
        for (int i = 1; i < length - n + 1; i++) {
            // cur 被删节点的前一个
            cur = cur.next;
        }
        cur.next = cur.next.next;
        return dummy.next;
    }

    public int getLength(ListNode head) {
        int length = 0;
        while (head != null) {
            ++length;
            head = head.next;
        }
        return length;
    }
}
```
