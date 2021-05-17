### 法一：双指针，找到要翻转的链表，翻转后再拼接   

```java
class Solution {
    public ListNode reverseBetween(ListNode head, int m, int n) {
        ListNode dummy = new ListNode(0);
        dummy.next = head;
        ListNode pre = dummy;

        // pre 定位到反转的起始位置即 m位置 的前驱节点
        for (int i = 1; i < m; i++) {
            pre = pre.next;
        }

        // head 指向需要反转部分的头节点
        head = pre.next;
        for (int i = m; i < n; i++) {
            ListNode nex = head.next;
            // head 把nex节点后的 链表连接起来,相当于 head后移一位
            head.next = nex.next;
            // nex节点插入到pre后面，即nex节点移动到反转部分的头部
            nex.next = pre.next;
            // pre 保持不变，作为反转部分的前驱
            pre.next = nex;
        }
        return dummy.next;
    }
}
```


### 法二：三指针      
参考：https://leetcode-cn.com/problems/reverse-linked-list-ii/solution/liang-chong-fang-fa-by-powcai/  

```python
class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        dummy = ListNode(-1)
        dummy.next = head
        pre = dummy

        for _ in range(m - 1):
            pre = pre.next
        
        #   1->2->3   2->1->3
        start = pre.next
        tail = start.next
        for _ in range(n - m):
            start.next = tail.next
            tail.next = pre.next
            pre.next = tail
            tail = start.next
        
        return dummy.next
```
start,tail