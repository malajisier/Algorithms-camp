# 递归法，88ms
# TS:O(n) , SC:O(n)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        def helper(node, lower = float('-inf'), upper = float('inf')):
            if not node:
                return True
            
            val = node.val
            if val <= lower or val >= upper:
                return False

            # 下探右子树时，当前结点的根结点作为下界，与之进行对比大小
            if not helper(node.right, val, upper):
                return False
            if not helper(node.left, lower, val):
                return False
            
            return True
        
        return helper(root)