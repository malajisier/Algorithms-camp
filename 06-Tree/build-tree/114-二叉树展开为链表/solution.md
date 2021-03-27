#### 法一：前序遍历   
要求单链表的顺序 = 前序序列
当二叉树展开为链表时 会破坏其结构，需要更新每个节点的左右子节点信息   

```java
// 递归实现
class Solution {
    public void flatten(TreeNode root) {
        List<TreeNode> list = new ArrayList<>();
        preorder(root, list);
        int size = list.size();

        for (int i = 1; i < size; i++) {
            TreeNode cur = list.get(i);
            TreeNode prev = list.get(i - 1);
            prev.left = null;
            prev.right = cur;
        }
    }

    public void preorder(TreeNode root, List<TreeNode> list) {
        if (root != null) {
            list.add(root);
            preorder(root.left, list);
            preorder(root.right, list);
        }
    }
}


// 迭代实现
class Solution {
    public void flatten(TreeNode root) {
        List<TreeNode> list = new ArrayList<TreeNode>();
        Deque<TreeNode> stack = new LinkedList<TreeNode>();
        TreeNode node = root;

        while (node != null || !stack.isEmpty()) {
            while (node != null) {
                list.add(node);
                stack.push(node);
                node = node.left;
            }
            node = stack.pop();
            node = node.right;
        }
        
        int size = list.size();
        for (int i = 1; i < size; i++) {
            TreeNode prev = list.get(i - 1), curr = list.get(i);
            prev.left = null;
            prev.right = curr;
        }
    }
}
```


#### 法二：前序遍历、展开 同步进行
```python
class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root: return 
        stack = [root]
        pre = None

        while stack:
            cur = stack.pop()
            if pre:
                pre.left = None
                pre.right = cur

            left, right = cur.left, cur.right
            # 右子节点需要先入栈，因为是后出栈
            if right: stack.append(right)
            if left: stack.append(left)

            pre = cur

```