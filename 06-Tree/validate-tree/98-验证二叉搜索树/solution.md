### 法一：递归实现

```java
class Solution {
    public boolean isValidBST(TreeNode root) {
        return isValidBST(root, Long.MIN_VALUE, Long.MAX_VALUE);
    }
    
    public boolean isValidBST(TreeNode node, long lower, long upper) {
        if (node == null) {
            return true;
        }
        if (node.val <= lower || node.val >= upper) {
            return false;
        }
		
        // 左右子树必须同时满足 BST
        return isValidBST(node.left, lower, node.val) && isValidBST(node.right, node.val, upper);
    }
}
```





### 法二：中序遍历有序

```java
class Solution {
    public boolean isValidBST(TreeNode root) {
        Deque<TreeNode> stack  = new LinkedList<>();
        long inorder = Long.MIN_VALUE;

        while (!stack.isEmpty() || root != null) {
            while (root != null) {
                stack.push(root);
                root = root.left;
            }
            
            root = stack.pop();
            // 当前值小于 前面的inorder，说明是非顺序
            if (root.val <= inorder) {
                return false;
            }
            
            // 记录当前值
            inorder = root.val;
            root = root.right;
        }
        return true;
    }
}
```

