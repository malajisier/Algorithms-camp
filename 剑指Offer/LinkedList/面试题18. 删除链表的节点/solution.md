本题与《剑指offer》有一些不同：
- 本题输入的类型为：head: ListNode, val: int
- 剑指offer中，默认输入为 head: ListNode, val: ListNode，即删除val链表的某个节点


剑指offer原题：
https://leetcode-cn.com/problems/shan-chu-lian-biao-de-jie-dian-lcof/solution/cong-on-dao-o1-by-ml-zimingmeng/
```java
// 待删除节点是最后一个时，TC=O(n)，总的平均复杂度O(1), SC:O(1)
class Solution {
    public static ListNode deleteNode(ListNode head, ListNode val) {
        if (head == null || val == null) {
            return null;
        }

        // 待删除节点 不是尾节点，直接用下一位的值 覆盖掉待删除位置
        if (val.next != null) {
            ListNode next = val.next;
            val.val = next.val;
            val.next = next.next;        
        } else if (head == val) { // 待删除节点只有一个 是头节点
            head == null;       
        } else {                  // 待删除节点是尾节点
            ListNode cur = head;
            while (cur.next != val) {
                cur = cur.next;
            }
            cur.next = null;
        }

        return head;
    }
}
```


### 法一：单指针  
TC:O(n), SC:O(1)
```python
class Solution:
    def deleteNode(self, head: ListNode, val: int) -> ListNode:
        dummy = ListNode(0)
        dummy.next = head
        if head.val == val: 
            return head.next 

        while head and head.next:
            if head.next.val == val:   
                head.next = head.next.next
            head = head.next
        return dummy.next
```


### 法二：双指针
```java
class Solution {
    public ListNode deleteNode(ListNode head, int val) {
        ListNode dummy = new ListNode(-1);
        dummy.next = head;
        ListNode pre = dummy, cur = head;

        while (dummy != null) {
            if (cur.val == val) {
                pre.next = cur.next;
                break;
            }
            pre = cur;
            cur = cur.next;
        }
        return dummy.next;
    }
}
```