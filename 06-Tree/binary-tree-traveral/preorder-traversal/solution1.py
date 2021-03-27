class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return
        
        res = []
        stack = []

        while stack:
            node = stack.pop()
            res.append(node.val)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        return res
        