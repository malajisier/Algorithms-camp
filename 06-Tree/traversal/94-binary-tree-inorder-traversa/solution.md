#### 法一：迭代实现  
```java
class Solution {
    public List<Integer> inorderTraversal(TreeNode root) {
        List<Integer> res = new ArrayList<>();
        Stack<TreeNode> stack = new Stack<>();
        TreeNode cur = root;

        while (cur != null || !stack.isEmpty()) {
            if (cur != null) {
                stack.push(cur);
                cur = cur.left;
            }  else {
                cur = stack.pop();
                res.add(cur.val);
                cur = cur.right;
            }
        }
        return res;
    }
}
```   


```python
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        # 法二：迭代法，使用辅助栈
        res = []
        stack = []
        # p作为指针
        p = root

        while p or stack:
            # 先将左儿子全部压入栈中，最后p指向null，循环停止
            while p:
                stack.append(p)
                p = p.left
            
            p = stack.pop()
            res.append(p.val)
            # 指向右子树
            p = p.right
        
        return res

```


#### 法二：递归
```python
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        # 法一：递归
        res = []

        def helper(root):
            if not root:
                return
            helper(root.left)
            res.append(root.val)
            helper(root.right)

        helper(root)
        return res

```