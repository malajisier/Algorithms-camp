```java
class Solution {
    public int[] reversePrint(ListNode head) {
        Stack<ListNode> s = new Stack<>();
        ListNode cur = head;
        while (cur != null) {
            s.push(cur);
            cur = cur.next;
        }

        int n = s.size();
        int[] res = new int[n];
        for (int i = 0; i < n; i++) {
            res[i] = s.pop().val;
        }
        return res;
    }
}
```