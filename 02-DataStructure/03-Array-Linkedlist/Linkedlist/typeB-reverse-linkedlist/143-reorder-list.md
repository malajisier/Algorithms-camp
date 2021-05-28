### 法一：辅助list  
- 链表不支持随机访问，使用辅助list 来通过下标访问  
- TC:O(N), SC:O(n)

```java
class Solution {
    public void reorderList(ListNode head) {
        if (head == null || head.next == null) {
            return;
        }
        List<ListNode> list = new ArrayList<>();
        while (head != null) {
            list.add(head);
            head = head.next;
        }

        int i = 0, j = list.size() - 1;
        while (i < j) {
            list.get(i).next = list.get(j);
            i++;
            if (i == j) break;
            list.get(j).next = list.get(i);
            j--;
        }
        list.get(i).next = null;
    }
}
```  



### 法二：中点截两段+逆序后半段+合并  
```java
class Solution {
    public void reorderList(ListNode head) {
        if (head == null || head.next == null) {
            return;
        }
        ListNode slow = head;
        ListNode fast = head;
        while (fast.next != null && fast.next.next != null) {
            slow = slow.next;
            fast = fast.next.next;
        }
        ListNode sideHead = slow.next;
        slow.next = null;
        sideHead = reverseList(sideHead);

        while (sideHead != null) {
            // tmp 指向 反转链表头的next节点
            ListNode tmp = sideHead.next;
            // sidehead 插到head 后面
            sideHead.next = head.next;
            head.next = sideHead;

            // 两个链表的头指针 分别后移
            head = sideHead.next;
            sideHead = tmp;
        } 
    }
    private ListNode reverseList(ListNode head) {
            if (head == null) {
                return null;
            }
            ListNode pre = null;
            ListNode cur = head;
            while (cur != null) {
                ListNode tmp = cur.next;
                cur.next = pre;
                pre = cur;
                cur = tmp;
            }
            return pre;
        }
}
```