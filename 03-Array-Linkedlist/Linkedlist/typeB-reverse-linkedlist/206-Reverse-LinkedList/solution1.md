### 法一：迭代实现
```java
class Solution {
    public ListNode reverseList(ListNode head) {
        ListNode pre = null;
        ListNode cur = head;
        while (cur != null) {
            // 记录 后一个节点
            ListNode next = cur.next;
            // 指向前一个节点，即反转
            cur.next = pre;
            // pre,cur 依次向后走
            pre = cur;
            cur = next;
        }
    }
}    
```  

```Python
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        pre = None
        cur = head
        
        while cur:
            tmp = cur.next
            cur.next = pre
            pre = cur
            cur = tmp
        return pre
```


### 法二：递归实现
有点绕，参考：
https://leetcode-cn.com/problems/reverse-linked-list/solution/dong-hua-yan-shi-206-fan-zhuan-lian-biao-by-user74/   

keys:
- 递归终止条件
- 反转节点的方法   
  
```python
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if head == None or head.next == None:
            return head

        # 递归一直往下走，从下往上一层层执行
        cur = reverseList(head.next)
        # 反转节点
        head.next.next = head
        # 设为空防止链表循环
        head.next = None

        return cur
```

