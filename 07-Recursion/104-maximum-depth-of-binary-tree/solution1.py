# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# 递归的DFS
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
         
        if root is None:
            return 0
        else:
            left_height = self.maxDepth(root.left)
            right_height = self.maxDepth(root.right)
            return max(left_height, right_height) + 1
        
        # C++
        # return (root == NULL)? 0 : max(maxDepth(root->left), maxDepth(root->right)) + 1