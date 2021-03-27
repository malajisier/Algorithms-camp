#### 法一：递归
```python
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:

        # 方法二：递归法
        res = []
        
        def helper(root):
            if not root:
                return
            res.append(root.val)
            helper(root.left)
            helper(root.right)

        helper(root)
        return res
```

#### 法二：迭代
模拟系统栈
```python
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        # 方法一：迭代法，使用辅助栈
        if not root:
            return 
        res = []
        stack = [root]

        while stack:
            node = stack.pop()
            res.append(node.val)
            # 先放入右节点，因为栈先入后出的特点
            if node.right:
                stack.append(node.right)
            
            # 先输出左结点
            if node.left:
                stack.append(node.left)
        return res
```