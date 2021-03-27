# 递归法，较为简单

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        res = []

        def helper(node):
            if not node:
                return         
            res.append(node.val)
            for child in node.children:
                helper(child)
            
        helper(root)
        return res


