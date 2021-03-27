#### 法一：严格按照后序遍历的访问顺序实现

写的非常好，推荐  
```java
class Solution {
    public List<Integer> postorderTraversal(TreeNode root) {
        List<Integer> res = new ArrayList<>();
        Stack<TreeNode> s = new Stack<>();
        Set<TreeNode> traversal = new HashSet<>();  // 存放遍历过的元素

        while (root != null || !s.isEmpty()) {
            if (root == null && traversal.contains(s.peek())) {
                res.add(s.pop().val);
            } else if (root == null) {
                traversal.add(s.peek());
                root = s.peek().right;
            } else {
                s.push(root);  // 先添加左子树
                root = root.left;
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
        
# 严格的 左右中遍历顺序
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
