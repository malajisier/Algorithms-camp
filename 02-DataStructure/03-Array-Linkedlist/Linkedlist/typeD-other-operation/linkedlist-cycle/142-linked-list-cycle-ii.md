### 法一：双指针   
https://leetcode-cn.com/problems/linked-list-cycle-ii/solution/linked-list-cycle-ii-kuai-man-zhi-zhen-shuang-zhi-/   

- f=2s （快指针每次2步，路程刚好2倍）  
- f = s + nb (相遇时，刚好多走了n圈），推出：s = nb  
- 从head结点走到入环点需要走 ： a + nb， 而slow已经走了nb，那么slow再走a步就是入环点了  
- 如何知道slow刚好走了a步？ 从head开始，和slow指针一起走，相遇时刚好就是a步  

```java
// SC:O(1) 
public class Solution {
    public ListNode detectCycle(ListNode head) {
        ListNode fast = head, slow = head;
        while (true) {
            if (fast == null || fast.next == null) return null;
            fast = fast.next.next;
            slow = slow.next;
            if (fast == slow) break;
        }
        fast = head;
        while (slow != fast) {
            slow = slow.next;
            fast = fast.next;
        }
        return fast;
    }
}
```   

```java
// 哈希表，O(n)

