参数：是需要删除的节点
用下一个位置的值 覆盖掉待删除位置，并指向下下一个的节点
```java
class Solution {
    public void deleteNode(ListNode node) {
        node.val = node.next.val;
        node.next = node.next.next;
    }
}
```