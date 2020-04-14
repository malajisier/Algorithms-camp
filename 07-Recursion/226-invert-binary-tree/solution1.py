# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return None
        # 先交换root的左右孩子
        root.left, root.right = root.right, root.left

        # 递归交换子节点的左右孩子
        self.invertTree(root.left)
        self.invertTree(root.right)

        return root