# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

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
            if node.left:
                stack.append(node.left)
        return res
