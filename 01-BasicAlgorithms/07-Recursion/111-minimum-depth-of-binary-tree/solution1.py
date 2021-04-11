# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# 题目的一个坑：叶子节点定义是没有子节点的节点
# 递归实现，TC: O(n), 空间复杂度最坏O(n),最佳O(logn)，所以平均SC:O(logn)

class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0
        
        children = [root.left, root.right]
        # 在叶子节点的时候
        if not any(children):
            return 1
        
        mindep = float('inf')
        for c in children:
            if c:
                mindep = min(self.minDepth(c), mindep)
        
        return mindep + 1