### 法一：迭代法     
- 按照严格的 左右中遍历顺序，
 

```java
class Solution {
    public List<Integer> postorderTraversal(TreeNode root) {
        LinkedList<Integer> res = new LinkedList<>();
        if (root == null) return res;
        
        ArrayDeque<TreeNode> stack = new ArrayDeque<>();
        TreeNode pre = null;

        while (root != null || !stack.isEmpty()) {
            // 走到左下节点
            while (root != null) {
                stack.push(root);
                root = root.left;
            }
            root = stack.pop();

            // 遍历最左节点的右子树
            if (root.right != null && root.right != pre) {
                stack.push(root);  // 重复压栈，记录分叉路径节点
                root = root.right;
            } else {
                res.add(root.val); // 当前节点的 左右子树都完成访问
                pre = root;        // 记录当前节点，方便下一步对比
                root = null;       // 重置root，避免重复访问左子树
            }
        }
        return res;
    }
}
```   

```python
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        if not root: return []
        res, stack = [], []
        prev = None

        while root or stack:
            while root:
                stack.append(root)
                root = root.left                  
            # 左子树走到头了，弹出最左节点
            root = stack.pop()

            # prev作用：标记访问过的节点，避免重复访问陷入死循环
            if not root.right or root.right == prev:
                # 弹出的节点添加到res，还需要重置节点root
                res.append(root.val)
                prev = root
                root = None
            else:
                stack.append(root)
                root = root.right

        return res
```


#### 法二：递归法    
```python

class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        # 递归法
        res = []

        def helper(root):
            if not root:
                return
            helper(root.left)
            helper(root.right)
            res.append(root.val)

        helper(root)
        return res
```
