# 题目：从上到下打印出二叉树的每个节点，同一层的节点按照从左到右的顺序打印

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# TC:O(N),N 为二叉树的节点数量
# SC:O(N), 最差情况下，即当树为平衡二叉树时，最多有N/2个树节点同时在 queue

class Solution:
    def levelOrder(self, root: TreeNode) -> List[int]:
        if not root: return []

        res, dq = [], collections.deque()
        dp.append(root)

        while dq:
            # popleft复杂度：O(1)
            node = dq.popleft()
            res.append(node.val)
            if node.left:
                dq.append(node.left)
            if node.right:
                dq.append(node.right)
        
        return res




        # 另一种写法：使用普通数组
        res, q = [], [root]
        while q:
            node = q.pop(0)
            res.append(node.val)