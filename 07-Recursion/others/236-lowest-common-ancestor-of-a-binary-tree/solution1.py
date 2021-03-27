# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root or root == p or root == q:
            return root
        
        # 只需找到一个节点，它的左右节点存在p、q
        left = lowestCommonAncestor(root.left, p, q)
        right = lowestCommonAncestor(root.right, p, q)

        if not left:
            return right
        if not right:
            return left

        return root        



    # def __init__(self):
    #         self.res = None

    # def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
    #     def recurse_tree(cur_node):
    #         if not cur_node:
    #             return False
            
    #         left = recurse_tree(cur_node.left)
    #         right = recurse_tree(cur_node.right)

    #         mid = cur_node == p or cur_node == q

    #         if mid + left + right >= 2:
    #             self.res = cur_node        
            
    #         return mid or left or right

    #     recurse_tree(root)
    #     return self.res