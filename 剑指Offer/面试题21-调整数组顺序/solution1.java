/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
class Solution {
    public ListNode getKthFromEnd(ListNode head, int k) {
        ListNode former = head, latter = head;

        // 头指针先走k-1步，然后头尾指针一起走，头指针走到最后一位时，尾指针。就指到了倒数第k个节点
        for (int i = 0; i < k - 1; i++) {
            former = former.next;
        }

        while (former.next != null) {
            former = former.next;
            latter = latter.next;
        }

        return latter;
    }
}