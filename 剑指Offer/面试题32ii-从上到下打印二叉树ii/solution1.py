# 题目：从上到下按层打印二叉树，同一层的节点按从左到右的顺序打印，每一层打印到一行


class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root: return []
        res, queue = [], [root]

        while queue:
            perLevel = []
            for _ in range(len(queue)):
                node = queue.pop(0)
                perLevel.append(node.val)
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)
            res.append(perLevel)
        
        return res