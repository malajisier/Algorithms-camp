### 法一：set集合去重    
set集合保证 一次出现
TC: O(n), SC:O(1)    

```java 
class Solution {
    public ListNode removeDuplicateNodes(ListNode head) {
        if (head == null) return head;
        Set<Integer> occurred = new HashSet<>();
        occurred.add(head.val);
        ListNode pos = head, cur = pos.next;

        while (pos.next != null) {
            if (occurred.add(cur.val)) {
                pos = pos.next;
            } else {
                pos.next = pos.next.next;
            }
            cur = cur.next;
        }

        return head;
    }
}
```   


### 法二：双指针
虽然不需要额外空间，但时间效率低
TC：O(n^2),  SC: O(1)    

```java
class Solution {
    public ListNode removeDuplicateNodes(ListNode head) {
        ListNode pos = head;
        while (pos != null) {
            // 固定一个数，再从头开始找
            ListNode cur = pos;
            while (cur.next != null) {
                if (cur.next.val == pos.val) {
                    cur.next = cur.next.next;
                } else {
                    cur = cur.next;
                }              
            }
            pos = pos.next;
        }
        return head;
    }
}
```