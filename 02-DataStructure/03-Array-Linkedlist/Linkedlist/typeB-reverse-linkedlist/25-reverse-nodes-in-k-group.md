进阶要求：  
- 常数级 的额外空间
- 不能单纯的只改变内部的值，必须交换节点

### 法一：辅助栈

- 翻转时 借助栈
- TC:O(n),  SC:O(k)，栈的固定输入规模是k，属于常数级

```python
class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        dummy = ListNode(-1)
        dummy.next = head
        p = dummy

        while True:
            count = k
            stack = []
            tmp = head
            while count and tmp:
                stack.append(tmp)
                tmp = tmp.next
                count -= 1
            
            # count还有剩余，说明tmp==null，k 大于 剩余链表长度
            # 根据要求，剩余的节点 不需要反转了
            if count:
                p.next = head
                break
            while stack:
                p.next = stack.pop()
                p = p.next
            
            # p 指向下一组 待反转的链表
            p.next = tmp
            # head 指向下一组的 head2
            head = tmp
        
        return dummy.next
```


### 法二：尾插法   
- 不借助额外空间，直接进行链表的节点交换，复杂一点
- TC:O(n),  SC:O(1)

```java
class Solution {
    public ListNode reverseKGroup(ListNode head, int k) {
        ListNode dummy = new ListNode(-1);
        dummy.next = head;
        ListNode pre = dummy;
        ListNode tail = dummy;

        while (true) {
            int count = 0;
            while (tail != null && count != k) {
                count++;
                tail = tail.next; // tail 指向待反转链表的末尾节点
            }
            // 剩余节点 长度不够k，不需要反转
            if (tail == null) break;

            ListNode head1 = pre.next;
            // 开始反转
            while (pre.next != tail) {
                // cur 首先是head1，指向从头开始 每个待插到尾部的元素
                ListNode cur = pre.next;
                // 因为要把head1插到尾部，所以pre 需要接上head1 后面的剩余链表
                pre.next = cur.next;
                // cur 插到尾部，指向下一组链表 的head2(tail.next)
                cur.next = tail.next;
                // 尾部的元素 更新为cur
                tail.next = cur;
            }
            // head1翻转后 就在最后一位，即第二组head2 的pre
            pre = head1;
            tail = head1;
        }
        return dummy.next;
    }
}
```