```python
# 递归实现
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        def recur(inL, inR):
            if inL > inR: return None
            
            # 通过后序序列，确定根节点位置及索引 
            val = postorder.pop()
            root = TreeNode(val)
            idx = idxMap[val]

            root.right = recur(idx + 1, inR)
            root.left = recur(inL, idx - 1)
            return root

        idxMap = {val:idx for idx, val in enumerate(inorder)}
        return recur(0, len(inorder) - 1)
```



```java
// 迭代实现，较难理解，没搞懂
// 和 105-前序中序构建二叉树  的迭代方法很像，但题解的解释乱七芭蕉
class Solution {
    public TreeNode buildTree(int[] inorder, int[] postorder) {
        int inSize = inorder.length, postSize = postorder.length;
        if (postorder == null || postSize == 0) {
            return null;
        }

        TreeNode root = new TreeNode(postorder[postSize - 1]);
        Deque<TreeNode> stack = new LinkedList<>();
        stack.push(root);
        int inIdx = inSize - 1; // 

        for (int i = postSize - 2; i >= 0; i--) {
            int postVal = postorder[i]; // 右子树
            TreeNode node = stack.peek();
            if (node.val != inorder[inIdx]) {
                node.right = new TreeNode(postVal);
                stack.push(node.right);
            } else {
                while (!stack.isEmpty() && stack.peek().val == inorder[inIdx]) {
                    node = stack.pop();
                    inIdx--;
                }
                node.left = new TreeNode(postVal);
                stack.push(node.left);
            }
        }
        return root;
    }
}
```